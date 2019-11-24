import logging

from django.http import HttpResponse

from common.utility import get_time_stamp, get_usd_jpy
from compare_project.settings import Session
from sqlalchemy_model.models import UsdJpy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _insert_usd_jpy(time_stamp, usd_jpy):
    logger.info('time_stamp={}, usd_jpy={}'.format(time_stamp, usd_jpy))
    record = UsdJpy(time_stamp=time_stamp, usd_jpy=usd_jpy)
    Session.add(record)
    Session.commit()


def get_fx_rate(request):
    if request.method != 'GET':
        return HttpResponse('error', content_type='text/plain')
    time_stamp = get_time_stamp()
    usd_jpy = get_usd_jpy()
    res = 'time_stamp={}, usd_jpy={}'.format(time_stamp, usd_jpy)
    _insert_usd_jpy(time_stamp=time_stamp, usd_jpy=usd_jpy)
    return HttpResponse(res, content_type='text/plain')
