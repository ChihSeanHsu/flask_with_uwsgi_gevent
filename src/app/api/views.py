import decimal
import os
from gevent import monkey, spawn
monkey.patch_all()

import boto3
import botocore.session

from flask import Blueprint, request, current_app as app

from api.logger import get_logger

logger = get_logger(__name__)

routes = Blueprint(
    'api', __name__,
    template_folder='templates',
    static_folder='static'
)

@routes.route('/ping', methods=['GET'])
def ping() -> (str):
    logger.debug('pong')
    return 'pong'

def get_item(pri: str, sec: int) -> (dict):
    db = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://dynamodb-local:8000')
    table = db.Table(os.environ.get('DYNAMODB_TABLE', 'ut_table'))
    res = table.get_item(Key={
        'primary': pri,
        'second': sec
    })
    return res

@routes.route('/get_dy/<string:primary>/<int:second>', methods=['GET'])
def get_dy(primary: str, second: int) -> (str):

    res = spawn(get_item(primary, second))
    data = res.get('Item', {})
    logger.info(data)
    return data
