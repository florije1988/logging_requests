# -*- coding: utf-8 -*-
__author__ = 'florije'


class CustomEx(Exception):

    """全渠道银联支付错误
    """
    # def __init__(self, *args):
    #     self.args = [arg for arg in args]


if __name__ == '__main__':
    try:
        raise CustomEx(1, 2, 3)
    except Exception as e:
        print e.args