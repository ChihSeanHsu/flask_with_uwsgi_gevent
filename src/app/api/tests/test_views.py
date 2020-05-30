import boto3
import json
import os
import pytest
import time


from decimal import Decimal
from unittest import mock

from .. import application

DB = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://dynamodb-local:8000')
TABLE = DB.Table(os.environ.get('DYNAMODB_TABLE', 'ut_table'))

@pytest.fixture
def test_client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client

def test_ping(test_client):
    res = test_client.get('/ping')
    assert b'pong' == res.data, 'health check api fail'

def test_get_dy(test_client):
    item = {
        'primary': 'a',
        'second': 1,
        'attr': 'test'
    }
    TABLE.put_item(
        Item=item
    )
    res = test_client.get('/get_dy/a/1')
    assert item == json.loads(res.data), 'get_dy api fail'