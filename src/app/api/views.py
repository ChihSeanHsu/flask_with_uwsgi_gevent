from gevent import monkey, spawn
monkey.patch_all()

import boto3
import botocore.session
import os
import simplejson as json
from flask import Blueprint, request, current_app as app
from api.logger import get_logger

import time

logger = get_logger(__name__)

routes = Blueprint(
    'api', __name__,
    template_folder='templates',
    static_folder='static'
)

KWARGS_FOR_DYNAMODB = {
    'region_name': os.environ.get('REGION', 'ap-northeast-1')
}
TABLE = os.environ.get('DYNAMODB_TABLE', 'ut_table')
if os.environ.get('ENV', 'DEV') == 'LOCAL':
    KWARGS_FOR_DYNAMODB['endpoint_url'] = 'http://dynamodb-local:8000'

session = botocore.session.get_session()
client = session.create_client(
    'dynamodb', **KWARGS_FOR_DYNAMODB)

@routes.route('/ping', methods=['GET'])
def ping() -> (str):
    logger.debug('pong')
    return 'pong'

def get_item(pri: str, sec: int) -> (dict):
    data = {}
    try:
        res = client.get_item(TableName=TABLE,
            Key={
                'primary': {
                    'S': pri
                },
                'second': {
                    'N': str(sec)
                }
            }
        )
        data = res.get('Item', {})
        
    except Exception as e: 
        logger.exception(e)

    return data


@routes.route('/get_dy/<string:primary>/<int:second>', methods=['GET'])
def get_dy(primary: str, second: int) -> (str):
    data = get_item(primary, second)
    logger.info(data)
    
    return data
