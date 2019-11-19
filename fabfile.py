from fabricio import docker, tasks

app = tasks.DockerTasks(
    service=docker.Container(
        name='app',
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