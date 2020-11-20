#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" """
__version__ = "1.0"
__history__ = """ """
__all__ = []


def merge_sorted(left, right, count):
    """将两个已排序的数组进行合并
    :param left 左数组
    :param right 右数组
    """
    print("[merge] 合并两个已排序的数组")
    array = []
    lengthl = len(left)
    lengthr = len(right)
    l = r = 0
    while l<lengthl and r<lengthr:
        if left[l] >= right[r]:
            array.append(left[l])
            if left[l] > right[r]:
                count += (lengthr - r)
            l += 1
        else:
            array.append(right[r])
            r += 1
    array.extend(left[l:])
    array.extend(right[r:])
    return array, count

def nixudui(array):
    '''逆序对'''
    """归并排序, 两两归并"""
    print("[merge] 归并排序")
    def _run(array):
        length = len(array)
        if length == 1:
            return array, 0
        key = int(length/2)
        left, countl = _run(array[:key])
        right, countr = _run(array[key:])
        return merge_sorted(left, right, countl + countr)
    return _run(array)
l = [0,5,2,8,4,9,1,7]
a,c = nixudui(l)
print(c)
