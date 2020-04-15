#!/bin/bash -l

set -e

# handle user override
NB_GID=${NB_UID}
PATH=${PATH//jovyan/$NB_USER}
USER_HOME="/home/$NB_USER"

# add a new group for the user
groupadd -g $NB_GID -o ${NB_GROUP:-${NB_USER}}

# add the user and set their home directory
useradd --home ${USER_HOME} -u $NB_UID -g $NB_GID -G 100 -l $NB_USER

# copy the content from the default docker image to the user home directory
shopt -s dotglob
cp -r --no-clobber /home/jovyan/* ${USER_HOME}

# set correct permissions for the user home directory
chown -R ${NB_USER}:${NB_USER} ${USER_HOME}

# link the read-only data volume
DATA="${USER_HOME}/data"
if [[ -e  ${DATA} ]]; then
    rm ${DATA}
fi
ln -s /srv/data ${DATA}

# execute the notebook process as the given user
exec su - $NB_USER -m -c '"$0" "$@"' -- "$@"
