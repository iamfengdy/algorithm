#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" """
__version__ = "1.0"
__history__ = """ """
__all__ = ["insert_base",
           "insert_base_while",
           "insert_directly",
           "insert_recursion",
           "insert_shell"]


from common import decorator


@decorator('basic for')
def insert_base(array):
    return _insert_base(array)


def _insert_base(array):
    """
    :param array: unsorted array
    :return:
    """
    for i in range(1, len(array)):
        temp = array[i]
        for j in range(i-1, -1, -1):
            if array[j] >= temp:
                array[j], array[j+1] = array[j+1], array[j]
                continue
            break
    return array


@decorator('basic while')
def insert_base_while(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1
        while array[j] > temp and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array


def position_directly(array, position, value):
    if array[position] < value:
        while array[position] < value:
            position += 1
    elif array[position] > value:
        while array[position] > value and position >= 0:
            position -= 1
        position += 1
    return position


def position_dichotomy(array, left, right, value):
    while left != right:
        temp = int((right+left)/2)
        if array[temp] >= value:
            right = temp
        else:
            left = (temp+1) if (right-left) == 1 else temp
    return left if array[left] >= value else (left+1)


def _insert2(array, method="directly"):
    """
    :param array:
    :param method: directly/dichotomy
    :return: 
    """
    position = 0
    for i in range(1, len(array)):
        temp = array[i]
        if method == "directly":
            position = position_directly(array, position, temp)
        else:
            position = position_dichotomy(array, 0, i-1, temp)
        for j in range(i, position, -1):
            array[j] = array[j-1]
        array[position] = temp
    return array


@decorator('directly')
def insert_directly(array):
    """
    set up a guard to indicate the location or data value that was inserted last time
    :param array:
    :return:
    """
    return _insert2(array, method="directly")


@decorator('dichotomy')
def insert_dichotomy(array):
    return _insert2(array, method='dichotomy')


@decorator('recursion')
def insert_recursion(array):
    """
    if u want to sort A[1..., n], sort A1[1..., n-1] firstly.
    :param array:
    :return:
    """

    def _insert_to_sorted(_array, value):
        for i in range(len(_array)):
            if value <= _array[i]:
                _array.insert(i, value)
                return _array
        _array.append(value)
        return _array

    def _run(_array):
        if len(_array) == 1:
            return _array
        prev = _run(_array[:-1])
        return _insert_to_sorted(prev, _array[-1])
    return _run(array)


@decorator('shell(Reduced incremental sort)')
def insert_shell(array):
    length = len(array)
    increment = int(length/2)
    while increment >= 1:
        index_array = [i for i in range(0, length, increment)]
        temp_array = [array[i] for i in index_array]
        temp_array = _insert_base(temp_array)
        for i in index_array:
            array[i] = temp_array[int(i/increment)]
        temp_array.clear()
        increment = int(increment/2)
    return array


def insert_shell_v2(array):
    """ TODO: Improved version
    Assuming that increment is d, then in the array A[d1,...,d2], A[d1] >= A[d2],
    so we only need to sort A[d1+1, ..., dn-1]
    """
    return array
