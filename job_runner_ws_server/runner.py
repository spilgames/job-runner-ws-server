import logging

import gevent
import geventwebsocket
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue

from job_runner_ws_server.events import consume
from job_runner_ws_server.websockets import WebSocketRequest, broadcast


logger = logging.getLogger(__name__)


def run(events_port, ws_port):
    """
    Start consuming and broadcasting events to WebSocket connections.

    :param events_port:
        The port to listen on for event.

    :param ws_port:
        The port to start the WebSocket server on.

    """
    ws_connect_queue = Queue()
    ws_disconnect_queue = Queue()
    event_queue = Queue()

    logger.info('Starting with consuming events on port {0}'.format(
        events_port))
    gevent.spawn(consume, events_port, event_queue)

    logger.info('Starting WebSocket broadcasting loop')
    gevent.spawn(broadcast, ws_connect_queue, ws_disconnect_queue, event_queue)

    logger.info('Starting WebSocket server on port {0}'.format(ws_port))
    WSGIServer(
        ('', ws_port),
        WebSocketRequest(ws_connect_queue, ws_disconnect_queue),
        handler_class=geventwebsocket.WebSocketHandler
    ).serve_forever()
