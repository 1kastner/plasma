User Environments
=================

User environments are built as immutable `Docker images <https://docs.docker.com/engine/docker-overview>`_.
The Docker images bundle the dependencies, extensions, and predefined notebooks that should be available to all users.

Plasma relies on the `tljh-repo2docker <https://github.com/plasmabio/tljh-repo2docker>`_ plugin to manage environments.
The ``tljh-repo2docker`` uses `jupyter-repo2docker <https://repo2docker.readthedocs.io>`_ to build the Docker images.

Environments can be managed by admin users by clicking on ``Environments`` in the navigation bar:

.. image:: ../images/environments/services-navbar.png
   :alt: Manage the list of environments
   :width: 50%
   :align: center

.. note::

  The user must be an **admin** to be able to access and manage the list of environments.


The page will show the list of environments currently available:

.. image:: ../images/environments/environments.png
   :alt: List of built environments
   :width: 100%
   :align: center


After a fresh install, this list will be empty.


Managing User Environments
--------------------------


.. toctree::
   :maxdepth: 3

   prepare
   add
   remove
   update
