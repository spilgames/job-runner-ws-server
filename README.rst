Job-Runner WebSocket Server
===========================

The WebSocket Server for the Job-Runner is a broadcaster for incoming events
published by the Job-Runner Workers. It's purpose is to collect events from
all available Job-Runner Workers and distribute these events through a
WebSocket server.


Installation
------------

This package can be installed by executing ``pip install job-runner-ws-server``.


Usage
-----

The usage of the ``job_runner_ws_server`` executable is::

    usage: job_runner_ws_server [-h] [--events-port EVENTS_PORT]
                                [--ws-port WS_PORT]
                                [--log-level {debug,info,warning,error}]

    Job-Runner WebSocket Server

    optional arguments:
      -h, --help            show this help message and exit
      --events-port EVENTS_PORT
                            The port to receive (worker) events on (default: 5555)
      --ws-port WS_PORT     The port for the WebSocket server (default: 5000)
      --log-level {debug,info,warning,error}
                            The log-level for logging (default: info)


Changes
-------

v0.5.0
~~~~~~

* Initial release.
