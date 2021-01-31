"""
PROJECT 6 - Priority Queues and Heaps
Name:
"""


class Node:
    """
    This class represents a node object with k (key) and v (value)
    Node definition should not be changed in any way
    """

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """

    def __init__(self, is_min=True):
        """
        Initializes the priority heap
        """
        self._data = []
        self.min = is_min

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Modify below this line


#These helper functions were taken right from onsay's lecture notes

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def empty(self):
        """
        Checks if the priority queue is empty
        :return: True is empty, false if not
        """
        return len(self._data) == 0

    def top(self):
        """
        Returns the root value
        :return: the root value, none otherwise
        """
        if not self.empty():
            return self._data[0].value

    def push(self, key, val):
        """
        Adds a node to the heap
        :key: the key to push
        :value: the value of the key to push
        :return: None
        """
        new_node = Node(key, val)
        self._data.append(new_node)
        index = len(self._data)-1
        self.percolate_up(index)

    def pop(self):
        """
        Removes the top element from the priority queue
        :return: None
        """
        if self.empty():
            return None

        self._swap(0, len(self._data)-1)
        item = self._data.pop()  # and remove it from the list;
        self.percolate_down(0)  # then fix new root
        return item


    def min_child(self, index):
        """
        Given an index of a node, return the index of the smaller child.
        :return: The index of the min child
        """
        if self._has_left(index):
            left = self._left(index)
            small_child = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] < self._data[left] or self._data[right] == self._data[left]:
                    small_child = right
            return small_child
        else:
            return None

    def max_child(self, index):
        """
        Given an index of a node, return the index of the bigger child.
        :return: The index of the max child
        """
        if self._has_left(index):
            left = self._left(index)
            big_child = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] > self._data[left] or self._data[right] == self._data[left]:
                    big_child = right
            return big_child
        else:
            return None

    def percolate_up(self, index):
        """
        Given the index of a node, move the node up to its valid spot in the heap.
        :return: None
        """
        if self.min:
            parent = (index - 1) // 2
            if index > 0 and self._data[index] < self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                self.percolate_up(parent)
        else:
            parent = (index - 1) // 2
            if index > 0 and self._data[index] > self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                self.percolate_up(parent)

    def percolate_down(self, index):
        """
        Given the index of a node, move the node down to its valid spot in the heap.
        :return: None
        """
        if self.min:
            if self._has_left(index):
                left = self._left(index)
                small_child = left
                if self._has_right(index):
                    right = self._right(index)
                    if self._data[right] < self._data[left]:
                        small_child = right
                if self._data[small_child] < self._data[index]:
                    self._swap(index, small_child)
                    self.percolate_down(small_child)
        else:
            if self._has_left(index):
                left = self._left(index)
                small_child = left
                if self._has_right(index):
                    right = self._right(index)
                    if self._data[right] > self._data[left]:
                        small_child = right
                if self._data[small_child] > self._data[index]:
                    self._swap(index, small_child)
                    self.percolate_down(small_child)



def heap_sort(array):
    """
    Given a list of data, use heap sort to sort the data
    :array: A list of data to sort
    :return: The sorted array
    """
    max_heap = PriorityHeap(False)
    for item in array:
        max_heap.push(item, item)
    n = len(max_heap)
    temp = []
    for j in range(n):
        to_add = max_heap.pop()
        temp.append(to_add.key)
    temp.reverse()
    return temp



def current_medians(values):
    """
    Keeps track of the median value of a list, creates a list of all median values
    :values: A list of numerical values
    :return: list of current medians of the data in the order it was given in
    """
