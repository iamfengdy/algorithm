#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" """
from pip._vendor.distlib.compat import raw_input

from copy import deepcopy
import timeit
from common import array2string, mylog
from sorter import (
    insertion,
    selection,
    merger,
    interchange,
)
from searcher import dichotomy

__version__ = "1.0"
__history__ = """ """
__all__ = []


def sorter_log(action_type=""):
    def _func(func):
        def __func(array, *args, **kwargs):
            mylog.info("[sort algorithm] %s" % action_type)
            mylog.info(">>unsorted：%s" % array2string(array))
            for sorter in func():
                try:
                    mylog.info(">>sorted：%s" % array2string(sorter(deepcopy(array))))
                except Exception as e:
                    mylog.error(e)
        return __func
    return _func


def searcher_log(action_type=""):
    def _func(func):
        def __func(*args, **kwargs):
            mylog.info("[search algorithm] %s" % action_type)
            position = func(*args, **kwargs)
            mylog.info('search result: ' + position)
        return __func
    return _func


@sorter_log("insertion")
def insertion_sorter():
    return (
        insertion.insert_base,
        insertion.insert_base_while,
        insertion.insert_directly,
        insertion.insert_dichotomy,
        insertion.insert_recursion,
        insertion.insert_shell,
    )


@sorter_log("selection")
def selection_sorter():
    return (
        selection.select_base,
    )
    # select.select(array)
    # select.build_min_heap(array)
    # selection.heapify_base(array)
    # print(selection.queue_min(array))
    # selection.heapify_base(array)
    # print(selection.quue_extract(array))
    # select.queue_insert(array, 10)
    # select.queue_decrease(array, 6, 10)


@sorter_log("interchange")
def interchange_sorter():
    return (
        interchange.bubble_base,
        interchange.bubble_bothway,
        interchange.bubble_flag,
        interchange.bubble_position,
        interchange.bubble_up_and_down,
        interchange.quick_base,
    )


@sorter_log("merger")
def merger_sorter():
    return (
        merger.merge_base,
        # merger.merge_sorted,
    )


@searcher_log("二分查找")
def find_erfen(array, goal):
    i = goal
    mylog.info("[any] value:{}, index:{}".format(str(i), str(dichotomy.erfen(array, i))))
    mylog.info("[first] value:{}, index:{}".format(str(i), str(dichotomy.erfen(array, i, "first"))))
    mylog.info("[last] value:{}, index:{}".format(str(i), str(dichotomy.erfen(array, i, "last"))))
    mylog.info("[all] value:{}, index:{}".format(str(i), str(dichotomy.erfen(array, i, "all"))))


def generate_random_array(length, max_value):
    """
    :param length: the length of array
    :param max_value: the array values range from 0 to max_value
    :return: unsorted array
    """
    import random
    array = []
    while len(array) < length:
        i = random.randint(1, max_value)
        if i not in array:
            array.append(i)
    return array


def run(array):
    # array = generate_random_array(10, 100)
    # insertion_sorter(array)
    # interchange_sorter(array)
    # merger_sorter(array)
    # selection_sorter(array)
    find_erfen(array, 10)
    pass


if __name__ == "__main__":
    # user_input = raw_input('Enter numbers separated by a comma:').strip()
    # unsorted = [int(str(item), 10) for item in user_input.split(',') if item]
    unsorted = [3, 6, 4, 2, 84, 856, 863, 3, 5]
    unsorted = generate_random_array(10, 100)
    run(deepcopy(unsorted))
    # tm = timeit.Timer("run()", setup="from __main__ import run")
    # mylog.info(">>时间："+str(tm.timeit(1)))


