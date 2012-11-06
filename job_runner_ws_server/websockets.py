import logging

from gevent.queue import Empty


logger = logging.getLogger(__name__)


def broadcast(connect_queue, disconnect_queue, event_queue):
    """
    Broadcast enqueued events to the connected websockets.

    :param connect_queue:
        A ``Queue`` instance for new connections.

    :param disconnect_queue:
        A ``Queue`` instance for disconnected websockets.

    :param event_queue:
        A ``Queue`` instance for events to broadcast.

    """
    sockets = []

    for event in event_queue:
        while True:
            try:
                sockets.append(connect_queue.get_nowait())
            except Empty:
                break

        while True:
            try:
                sockets.remove(disconnect_queue.get_nowait())
            except Empty:
                break

        for socket in sockets:
            try:
                socket.send(event)
            except Exception:
                logger.exception('Sending message failed')


class WebSocketRequest(object):
    def __init__(self, connect_queue, disconnect_queue):
        self.connect_queue = connect_queue
        self.disconnect_queue = disconnect_queue

    def __call__(self, environ, start_response):
        logger.debug('Incoming WS connection')
        websocket = environ.get('wsgi.websocket')

        if not websocket:
            start_response('400 Bad Request', [])
            return ["WebSocket connection is expected."]

        self.connect_queue.put(websocket)

        try:
            while True:
                message = websocket.receive()
                if not message:
                    break
            websocket.close()
        except Exception:
            logger.exception('Something went wrong')

        self.disconnect_queue.put(websocket)
        logger.debug('WS disconnected')
