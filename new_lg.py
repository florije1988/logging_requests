# -*- coding: utf-8 -*-
__author__ = 'florije'
# import logging
import logging.config
logging.basicConfig(filename="new_lg.log", level=logging.INFO)
import otherMod

# logging.basicConfig(filename="new_lg.log", level=logging.INFO)
# logging.basicConfig(filename='new_lg.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
# logging.config.fileConfig('new_lg_config.conf', disable_existing_loggers=False)
main_logger = logging.getLogger(__name__)


def main():
    main_logger.info("Program started")
    result = otherMod.add(7, 8)
    main_logger.info("Done!")


if __name__ == "__main__":
    main()
