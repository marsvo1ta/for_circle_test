import os

def test_simple():
    assert os.environ.get('TEST_VALUE') == 'TEST'
    