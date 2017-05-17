import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Base:
    SEND_FILE_MAX_AGE_DEFAULT = 1
    SECRET_KEY = b'\xb8`H\xe2\xec~\x9cs\x0eK\x1c\x9f\x90\x01\xec\xdbaI\xb9\xe0WG\xc6\r'
