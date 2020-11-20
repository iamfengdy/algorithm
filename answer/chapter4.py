#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Author:fengdy
# @Email:iamfengdy@126.com
# @DateTime:2019/4/29 14:15

""" look up the max and the max cross subarray """
__version__ = "1.0"
__history__ = """ """
__all__ = []



'''查找最大和连续子数组
'''
__history__ = ''''''
__all__ = []


def find_max(array, low, high):
    if low == high:
        return (low, high), array[low]
    # elif low > high:
    #     return (high, high), array[high]
    else:
        mid = int((low+high)/2)
        left_array, left_max = find_max(array, low, mid)
        right_array, right_max = find_max(array, mid+1, high)
        cross_array, cross_max = find_max_cross(array, low, mid, high)
        if left_max >= right_max and left_max >= cross_max:
            return left_array, left_max
        if right_max >= left_max and right_max >= cross_max:
            return right_array, right_max
        if cross_max >= left_max and cross_max >= right_max:
            return cross_array, cross_max


def find_max_cross(array, low, mid, high):
    left_sum = array[mid]
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + array[i]
        if sum >= left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    right_sum = array[mid+1]
    for j in range(mid+1, high+1):
        sum = sum + array[j]
        if sum >= right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right), left_sum+right_sum

class Node:
    def __init__(self, left, right, sum):
        self.left = left
        self.right = right
        self.sum = sum
    def __str__(self):
        return "({},{}), {}".format(self.left, self.right, self.sum)

def find_by_no_recursion(array, low, high):
    """ 课后题4.1-5
    :param array:
    :param low:
    :param high:
    :return:
    """
    if len(array) == 0:return None
    result = Node(low, low, array[0]) #表示array[0, j]中最大和子数组
    if len(array) == 1:return None
    for i in range(low+1, high+1):
        current = Node(i, i, array[i])  #表示array[i, j+1]中最大和子数组
        temp_sum = 0
        for j in range(i, result.right, -1):
            temp_sum += array[j]
            if temp_sum >= current.sum:
                current = Node(j, i, temp_sum)
            # print(current)
        if current.sum>=result.sum:
            if result.sum >= 0 and current.left == result.right+1:
                result = Node(result.left, current.right, result.sum+current.sum)
            else:
                result = current
        else:
            if current.sum >= 0 and current.left == result.right+1:
                result = Node(result.left, current.right, result.sum+current.sum)
        # print(result)
        # print("=")
    return result





array = [60, 2,-80,9,-20,8,9,17]
# array = [-23,-83,-9,-20,-8,-9,-17]
a, s = find_max(array, 0, len(array)-1)
print(a)
print(s)
print(find_by_no_recursion(array, 0, len(array)-1))




