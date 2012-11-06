from setuptools import setup

import job_runner_ws_server


setup(
    name='job-runner-ws-server',
    version=job_runner_ws_server.__version__,
    url='https://github.com/spilgames/dwh/',
    author='Orne Brocaar',
    author_email='orne.brocaar@spilgames.com',
    description='Job-Runner WebSocket Server',
    long_description=open('README.rst').read(),
    packages=[
        'job_runner_ws_server',
    ],
    scripts=[
        'scripts/job_runner_ws_server',
    ],
    install_requires=[
        'argparse',
        'gevent',
        'gevent_subprocess',
        'gevent-websocket',
        'pyzmq',
    ]
)
