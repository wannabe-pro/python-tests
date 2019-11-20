import functools

import fabricio

from fabric import api as fab, colors
from fabricio import tasks, docker, utils
from fabricio.misc import AvailableVagrantHosts

fab.env.roledefs.update(
    # you can set default roles definitions here
    web=['localhost'],
)

@fabricio.infrastructure(color=colors.red)
def vagrant():
    fab.env.update(
        roledefs={
            'web': AvailableVagrantHosts(),
        },
    )

@fabricio.infrastructure()
def localhost(force_local=True):
    if utils.strtobool(force_local):
        # replace fabricio.run by fabricio.local to run all commands locally
        fabricio.run = functools.partial(fabricio.local, capture=True)

        # uncomment row below to skip file uploading (e.g. docker-compose.yml)
        fab.put = lambda *args, **kwargs: None

    fab.env.update(
        roledefs={
            'web': ['localhost'],
        },
    )

app = tasks.DockerTasks(
    service=docker.Container(
        name='app',
        image='nginx',
        options={
            'publish': '80:80',
            'network': 'bridge'
        },
    ),
    roles=['web'],
    
    # rollback_command=True,  # show `rollback` command in the list
    # migrate_commands=True,  # show `migrate` and `migrate-back` commands in the list
    # backup_commands=True,  # show `backup` and `restore` commands in the list
    # pull_command=True,  # show `pull` command in the list
    # update_command=True,  # show `update` command in the list
    # revert_command=True,  # show `revert` command in the list
    # destroy_command=True,  # show `destroy` command in the list
)

selenium = tasks.DockerTasks(
    service=docker.Container(
        name='selenium',
        image='selenium/standalone-chrome',
        options={
            'publish': '4444:4444',
            'network': 'bridge'
        },
    ),
    roles=['web'],
    
    # rollback_command=True,  # show `rollback` command in the list
    # migrate_commands=True,  # show `migrate` and `migrate-back` commands in the list
    # backup_commands=True,  # show `backup` and `restore` commands in the list
    # pull_command=True,  # show `pull` command in the list
    # update_command=True,  # show `update` command in the list
    # revert_command=True,  # show `revert` command in the list
    # destroy_command=True,  # show `destroy` command in the list
)
