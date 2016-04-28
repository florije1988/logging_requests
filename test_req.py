# -*- coding: utf-8 -*-
__author__ = 'florije'

import requests
import logging
from logging.config import fileConfig
fileConfig('logging.conf', disable_existing_loggers=False)

# logging.getLogger("requests").setLevel(logging.WARNING)
# logging.basicConfig(level=logging.DEBUG, )
logger = logging.getLogger(__name__)

logger.info('something.')

r = requests.get('http://httpbin.org/get?foo=bar&baz=python')
print r.content