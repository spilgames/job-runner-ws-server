import logging

import zmq.green as zmq


logger = logging.getLogger(__name__)


def consume(events_port, event_queue):
    """
    Consume events coming in and put them in the event queue.

    :param events_port:
        The port to listen on for events.

    :param event_queue:
        A ``Queue`` instance, for putting the events in.

    """
    context = zmq.Context(1)
    subscriber = context.socket(zmq.SUB)
    subscriber.bind('tcp://*:{0}'.format(events_port))
    subscriber.setsockopt(zmq.SUBSCRIBE, 'worker.event')

    while True:
        address, content = subscriber.recv_multipart()
        logger.debug('Received [{0}]: {1}'.format(address, content))
        event_queue.put(content)

    subscriber.close()
    context.term()
