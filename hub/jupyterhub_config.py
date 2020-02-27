import logging
import os

from dockerspawner import DockerSpawner
from jupyterhub.auth import PAMAuthenticator
from jupyterhub_traefik_proxy import TraefikTomlProxy

# list of images to choose from when spawning a new server
IMAGES = {
    'python': 'jupyter/scipy-notebook',
    'r': 'jupyter/r-notebook',
}

# TODO: set back to logging.INFO
c.JupyterHub.log_level = logging.DEBUG

# hub
c.JupyterHub.hub_ip = 'hub'
c.JupyterHub.allow_named_servers = True
c.JupyterHub.proxy_class = TraefikTomlProxy
c.JupyterHub.authenticator_class = PAMAuthenticator
c.JupyterHub.spawner_class = DockerSpawner

# proxy
c.TraefikTomlProxy.should_start = False
c.TraefikTomlProxy.traefik_api_url = "http://proxy:8099"
# TODO: handle secrets. These can be generated automatically
c.TraefikTomlProxy.traefik_api_username = "foo"
c.TraefikTomlProxy.traefik_api_password = "bar"
c.TraefikTomlProxy.toml_static_config_file = "/srv/jupyterhub/proxy/traefik.toml"
c.TraefikTomlProxy.toml_dynamic_config_file = "/srv/jupyterhub/proxy/rules.toml"

# spawner
# increase the timeout to be able to pull larger Docker images
c.DockerSpawner.start_timeout=120
c.DockerSpawner.image_whitelist = IMAGES
c.DockerSpawner.network_name = os.getenv('DOCKER_NETWORK_NAME')
c.DockerSpawner.name_template = "{prefix}-{username}-{imagename}-{servername}"
c.DockerSpawner.default_url = '/lab'
c.DockerSpawner.remove = True
