from gevent import monkey
monkey.patch_all()

import unittest2 as unittest
import time

import gevent
import websocket
import zmq.green as zmq

from job_runner_ws_server.runner import run


class WebSocketServerTestCase(unittest.TestCase):
    """
    Tests for the WebSocket server.
    """
    def test_flow(self):
        """
        Test the full event to websocket flow.

        We start the :func:`.run` with the event listener on port 5555 and the
        WebSocket server on port 5000. Then we send an event and check we
        receive it in our WebSocket connection.

        .. note:: The coverage displayed by the coverage tool doesn't play
            nicely with gevent.

        """
        gevent.spawn(run, 5555, 5000)
        time.sleep(1)
        ws = websocket.create_connection('ws://localhost:5000/')

        context = zmq.Context(1)
        publisher = context.socket(zmq.PUB)
        publisher.connect('tcp://localhost:5555')
        publisher.send_multipart(['worker.event', 'foo-bar'])
        self.assertEqual('foo-bar', ws.recv())
