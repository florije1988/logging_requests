# -*- coding: utf-8 -*-
__author__ = 'florije'

import logging

logging.basicConfig(level=logging.INFO)  # filename="otherMod.log",
module_logger = logging.getLogger(__name__)


def add(x, y):
    # module_logger = logging.getLogger(__name__)
    module_logger.info("added %s and %s to get %s" % (x, y, x + y))
    return x + y
