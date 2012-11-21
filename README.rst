Job-Runner WebSocket Server
===========================

The WebSocket Server for the Job-Runner is a broadcaster for incoming events
published by the Job-Runner Workers. It's purpose is to collect events from
all available Job-Runner Workers and distribute these events to all the
connected WebSocket clients.


Installation
------------

Deployar
~~~~~~~~

This package is as ``job-runner-ws-server`` available in Deployar.


From source
~~~~~~~~~~~

If you are running the code from source, make sure you have the following
requirements installed:

   * ``python-devel``
   * ``gcc``
   * ``gcc-c++``
   * ``libevent-devel``

Then install the Python requirements with ``pip install -r requirements.txt``.


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

v1.0.0
~~~~~~

* Deployar related changes.


v0.5.0
~~~~~~

* Initial release.
