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


@decorator('basic')
def select_base(array):
    length = len(array)
    for i in range(length):
        key = i
        for j in range(i+1, length):
            if array[j] < array[key]:
                key = j
        array[i], array[key] = array[key], array[i]
    return array


# HEAP
PARENT = lambda i: int(i/2)  # Parent index
LEFT = lambda i: 2*i     # Left child node index
RIGHT = lambda i: (2*i+1)    # Right child node index


class Heap:
    def __init__(self, array):
        self.array = array
        self.size = len(array)-1    # The index starts at 0

    def exchange(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def build_minimum_heap(self):
        """build minimum heap
        :return:
        """
        for i in range(int(self.size/2), -1, -1):
            self.min_heapify(i)

    def min_heapify(self, index):
        """Maintenance minimum heap
        :param index: index
        :return:
        """
        left_index = LEFT(index)
        right_index = RIGHT(index)
        smaller = index
        if left_index <= self.size and self.array[left_index] < self.array[index]:
            smaller = left_index
        if right_index <= self.size and self.array[right_index] < self.array[smaller]:
            smaller = right_index
        if smaller != index:
            self.exchange(index, smaller)
            self.min_heapify(smaller)

    def heapify_base(self):
        self.build_min_heap()
        for i in range(self.size, 0, -1):
            self.exchange(0, i)
            self.size -= 1
            self.min_heapify(0)


class Queue(Heap):
    def minimum(self):
        return self.array[0]

    def extract(self):
        if self.size < 0:
            return None
        result = self.array[0]
        self.array[0] = self.array[self.size]
        self.size -= 1
        self.min_heapify(0)
        return result

    def decrease(self, node_index, value):
        """
        decrease Heap[node_index] to value
        :param node_index:
        :param value:
        :return:
        """
        if self.array[node_index] >= value:
            return None
        self.array[node_index] = value
        while node_index > 0 and self.array[PARENT(node_index)] > self.array[node_index]:
            self.exchange(node_index, PARENT(node_index))
            i = PARENT(node_index)

    def insert(self, value):
        self.size += 1
        # FIXME: This should be relative
        # FIXME: depending on the nature of the heap (maximum or minimum) and the nature of the elements
        self.array.append(0)
        self.decrease(self.size, value)
