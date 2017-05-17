import webview
from threading import Thread, Lock
import logging
from todo.server import run_server

server_lock = Lock()
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.debug('Starting Server')
    t = Thread(target=run_server)
    t.daemon = True
    t.start()
    logger.debug('Server has started.')
    webview.create_window('PyNash', 'http://localhost:8088', min_size=(640, 480))
