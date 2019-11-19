from fabricio import docker, tasks

nginx = tasks.DockerTasks(
    service=docker.Container(
        name='nginx',
        image='nginx',
        options={
            'publish': '80:80',
        },
    ),
)

selenium = tasks.DockerTasks(
    service=docker.Container(
        name='selenium',
        image='selenium/standalone-chrome',
        options={
            'publish': '4444:4444',
        },
    ),
)