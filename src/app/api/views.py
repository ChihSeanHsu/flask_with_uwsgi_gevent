import os
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
