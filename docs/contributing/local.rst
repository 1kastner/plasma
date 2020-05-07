Setting up a dev environment
============================

It is possible to test the project locally without installing TLJH. Instead we use the ``jupyterhub`` Python package.

Requirements
------------

``Docker`` is used as a ``Spawner`` to start the user servers, and is then required to run the project locally.

Check out the official Docker documentation to know how to install Docker on your machine:
https://docs.docker.com/install/linux/docker-ce/ubuntu/

Create a virtual environment
----------------------------

Using ``conda``:

.. code-block:: bash

  conda create -n plasma -c conda-forge python nodejs
  conda activate plasma

Alternatively, with Python's built in ``venv`` module, you can create a virtual environment with:

.. code-block:: bash

  python3 -m venv .
  source bin/activate

Install the development requirements
------------------------------------

.. code-block:: bash

  pip install -r dev-requirements.txt

  # dev install of the plasma package
  pip install -e tljh-plasma

  # Install (https://github.com/jupyterhub/configurable-http-proxy)
  npm -g install configurable-http-proxy

Pull the repo2docker Docker image
---------------------------------

User environments are built with ``repo2docker`` running in a Docker container. To pull the Docker image:

.. code-block:: bash

  docker pull jupyter/repo2docker

Run
---

Finally, start ``jupyterhub`` with the config in ``debug`` mode:

.. code-block:: bash

  python3 -m jupyterhub -f jupyterhub_config.py --debug

Open `https://localhost:8000 <https://localhost:8000>`_ in a web browser.
