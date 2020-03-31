import asyncio
import subprocess
import sys

from threading import Event
from urllib.parse import urlparse

import docker

from jupyterhub.services.auth import HubAuthenticated
from tornado import web, escape
from tornado.log import app_log

client = docker.from_env()


def build_image(repo, ref):
    """
    Build an image given a repo and a ref
    """
    ref = ref or "master"
    name = urlparse(repo).path.strip("/")
    image_name = f"{name}:{ref}"
    cmd = [
        "jupyter-repo2docker",
        "--ref",
        ref,
        "--user-name",
        "jovyan",
        "--user-id",
        "1100",
        "--no-run",
        "--image-name",
        image_name,
        "--appendix",
        f"LABEL repo2docker.display_name={name}-{ref}\nLABEL repo2docker.image_name={image_name}",
        repo,
    ]
    client.containers.run(
        "jupyter/repo2docker:master",
        cmd,
        labels={
            "repo2docker.repo": repo,
            "repo2docker.ref": ref,
            "repo2docker.build": image_name,
        },
        volumes={
            "/var/run/docker.sock": {"bind": "/var/run/docker.sock", "mode": "rw"}
        },
        detach=True,
        remove=True,
    )


def remove_image(name):
    """
    Remove an image by name
    """
    client.images.remove(name)


class BuildHandler(HubAuthenticated, web.RequestHandler):
    def initialize(self):
        self.log = app_log

    @web.authenticated
    def delete(self):
        self.log.debug("Delete an image")
        data = escape.json_decode(self.request.body)
        name = data["name"]
        # TODO: should this run in an executor? (removing the image is blocking)
        remove_image(name)
        self.set_status(200)

    @web.authenticated
    def post(self):
        self.log.debug("Build user images")

        data = escape.json_decode(self.request.body)
        repo = data["repo"]
        ref = data["ref"]
        # TODO: validate input
        build_image(repo, ref)

        self.set_status(200)
