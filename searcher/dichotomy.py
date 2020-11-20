#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" """
__version__ = "1.0"
__history__ = """ """
__all__ = []


def erfen(array, target_value, search_type=None):
    """dichotomy recursive search，return when finded
    :param array: must be a sorted array
    :param target_value: the target value to look for
    :type search_type:
        all: find all matched values
        first: find the first one matched values
        last: find the last one matched values
        None: any, default
    :return index of value or None
    """
    _from = 0
    _to = len(array)
    result = None
    search_type = search_type.lower() if search_type else None
    while _from < _to:
        key = int((_to+_from)/2)
        if array[key] > target_value and key < _to:
            _to = key
        elif array[key] == target_value:
            result = key
            if key <= _from or key >= _to or search_type is None:
                return result
            if search_type == "first":
                _to = key
            elif search_type == "last":
                _from = key
            elif search_type == "all":
                first = _from + (erfen(array[_from:key+1], target_value, search_type="first") or 0)
                last = result + (erfen(array[key:_to+1], target_value, search_type="last") or 0)
                return last-first+1
            else:
                return result
        elif array[key] < target_value and key > _from:
            _from = key
        else:
            return result
    return result


