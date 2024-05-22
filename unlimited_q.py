"""
Create a queue data structure that supports enqueue and dequeue operations, where 
the queue is composed of subarrays with a maximum size of 5 elements each.
"""

import logging
from collections import deque

class InvalidSubarraySize(Exception):
    def __init__(self, message="Invalid subarray size. Subarray size must be an integer greater than 1."):
        self.message = message
        super().__init__(self.message)

class QueueNode:
    def __init__(self, max_queue_size, next_node=None):
        if not isinstance(max_queue_size, int):
            raise TypeError("Max queue size provided is not an integer.")
        if max_queue_size < 1:
            raise InvalidSubarraySize()
        self.max_q_size = max_queue_size
        self.next_node = next_node
        self.q = deque()

    def size(self):
        return len(self.q)

    def is_full(self):
        return self.size() == self.max_q_size

    def is_empty(self):
        return self.size() == 0

    def add(self, val):
        if self.is_full():
            return False
        self.q.append(val)
        return True

    def remove(self):
        if self.is_empty():
            raise IndexError("Index out of range. Trying to remove from empty queue.")
        else:
            return self.q.popleft()

class UnlimitedQueue:
    def __init__(self, subarray_size):
        if not isinstance(subarray_size, int) or subarray_size < 1:
            raise InvalidSubarraySize("Subarray size must be an integer greater than 1.")
        self.subarray_size = subarray_size
        self.curr_node = QueueNode(self.subarray_size)
        self.total_elements = 0
        self.unlimited_queue_head = self.curr_node

    def enqueue(self, val):
        if self.curr_node.is_full():
            new_node = QueueNode(self.subarray_size)
            self.curr_node.next_node = new_node
            self.curr_node = new_node

        rc = self.curr_node.add(val)
        if rc:
            self.total_elements += 1
        
        return rc

    def dequeue(self):
        # check if UnlimitedQueue is completely empty
        if self.total_elements == 0:
            raise IndexError("Index out of range. Trying to remove from empty queue.")

        if self.unlimited_queue_head.is_empty():
            # Should never be hitting this code, if we do, then we’re not correctly updating self.total_elements
            if not self.unlimited_queue_head.next_node:
                raise IndexError("Index out of range. Trying to remove from empty queue.")
            else:
                # detach head node as it’s empty
                temp = self.unlimited_queue_head.next_node
                self.unlimited_queue_head.next_node = None
                self.unlimited_queue_head = temp
        
        self.total_elements -= 1
        return self.unlimited_queue_head.remove()

if __name__ == "__main__":
    uq = UnlimitedQueue('a')
        
    for i in range(1, 16):
        uq.enqueue(i)

    for _ in range(16):
        try:
            print(uq.dequeue())
        except IndexError as ex:
            logging.error(f"Error encountered while popping from unlimited queue: {ex}")
            
    for i in range(0, 4):
        uq.enqueue(i)
        
    for _ in range(7):
        try:
            print(uq.dequeue())
        except IndexError as ex:
            logging.error(f"Error encountered while popping from unlimited queue: {ex}")
