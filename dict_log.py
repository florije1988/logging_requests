# -*- coding: utf-8 -*-
__author__ = 'florije'

import time
import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'standard': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'console': {'class': 'logging.StreamHandler',
                    'formatter': 'standard',
                    'level': logging.DEBUG},
        'rotate_file': {
            'level': logging.DEBUG,
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'tmp.log',
            'encoding': 'utf-8',
            'when': 's'
        }
    },
    loggers={
        '': {'handlers': ['console', 'rotate_file'],
             'level': logging.DEBUG}
    }
)

dictConfig(logging_config)

logger = logging.getLogger(__name__)
logger.info('often makes a very good meal of %s', 'visiting tourists')

time.sleep(10)
logger.info('often makes a very good meal of %s', 'visiting tourists')