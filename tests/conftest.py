import os
import pytest
import uuid
import json
from binascii import unhexlify
from xbox.sg.crypto import Crypto


@pytest.fixture(scope='session')
def packets():
    # Who cares about RAM anyway?
    data = {}
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'packets')
    for f in os.listdir(data_path):
        with open(os.path.join(data_path, f), 'rb') as fh:
            data[f] = fh.read()

    return data
