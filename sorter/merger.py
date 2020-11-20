#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" """
__version__ = "1.0"
__history__ = """ """
__all__ = []


from common import mylog, array2string, decorator


@decorator('merge two sorted array')
def merge_sorted(left, right):
    return _merge_sorted_array(left, right)


def _merge_sorted_array(left, right):
    """
    :param left: sorted array
    :param right: sorted array
    """
    array = []
    left_length = len(left)
    right_length = len(right)
    left_index = right_index = 0
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            array.append(left[left_index])
            left_index += 1
        else:
            array.append(right[right_index])
            right_index += 1
    array.extend(left[left_index:])
    array.extend(right[right_index:])
    return array


@decorator('basic')
def merge_base(array):

    def _run(_array):
        length = len(_array)
        if length == 1:
            return _array
        key = int(length/2)
        left = _run(_array[:key])
        right = _run(_array[key:])
        return _merge_sorted_array(left, right)
    return _run(array)
        



