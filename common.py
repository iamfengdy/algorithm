#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" """
import os

__version__ = "1.0"
__history__ = """ """
# __all__ = []


try:
    import logging.config
    logging.config.fileConfig("logger.ini")
    mylog = logging.getLogger(__name__)
except:
    try:
        from units.log_unit import mylog
    except:
        import logging.config
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'result.log'),
            filemode='w')

        mylog = logging.getLogger(__name__)
        mylog.setLevel(logging.DEBUG)


def array2string(array):
    return ','.join(map(lambda x:str(x), array))


def decorator(func_name):
    def _func(func):
        def __func(*args, **kwargs):
            mylog.debug(func_name)
            return func(*args, **kwargs)
        return __func
    return _func

