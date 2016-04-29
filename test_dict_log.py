# -*- coding: utf-8 -*-
__author__ = 'florije'

import logging
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'stream_handler': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['stream_handler',],
            'level': 'DEBUG',
        },
    }
}
logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)
logger.info('often makes a very good meal of %s', 'visiting tourists')
