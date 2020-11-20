#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

"""interchange """
__version__ = "1.0"
__history__ = """ """
__all__ = []


from common import mylog, array2string, decorator


@decorator('bubble basic')
def bubble_base(array):
    length = len(array)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


@decorator('bubble flag')
def bubble_flag(array):
    """
    Improved version，add flag
    :param array:
    :return:
    """
    exchange = True     # boolean, Whether there is an exchange in one traversal
    length = len(array)
    while exchange:
        exchange = False
        for i in range(length-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                exchange = True
    return array


@decorator('bubble position')
def bubble_position(array):
    """
    Record the last swap position, iterate to this position next time
    :param array:
    :return:
    """
    position = len(array) - 1  # The last unsorted position
    while position > 0:
        prev = position
        for i in range(position):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                position = i
        position = 0 if position == prev else position
    return array


@decorator('bubble both way')
def bubble_bothway(array):
    """
    Improved version.
    The maximum and minimum values are obtained by bubbling forward and backward in each sort.
    Not applicable to sorted arrays
    :param array:
    :return:
    """
    length = len(array)
    # for i in range(int(length/2)+1):
    for i in range(length):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
        for j in range(i, length-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


@decorator('bubble up and down')
def bubble_up_and_down(array):
    """
    Improved version.
    Start with the biggest bubbling to the end,
    then come back with the smallest bubbling, and repeat the process until you're done.
    :param array:
    :return:
    """
    left = 0
    right = len(array)-1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
        left += 1
    return array


def _partition(array, left, right):
    """
    Select a benchmark, traverse and compare, and divide into two sections: large and small
    :param array:
    :param left: start index
    :param right end index
    :return: index of benchmark
    """
    base = array[right]     # Select a benchmark
    i = left - 1
    for j in range(left, right+1):
        if array[j] <= base:
            i += 1
            array[i], array[j] = array[j], array[i]
    return i


def _quick_sort(array, left, right):
    pt = _partition(array, left, right)
    if (pt-left) > 1:
        _quick_sort(array, left, pt-1)
    if (right-pt) > 1:
        _quick_sort(array, pt+1, right)
    return array


@decorator('quick basic')
def quick_base(array):
    return _quick_sort(array, 0, len(array)-1)
