"""
Create a queue data structure that supports enqueue and dequeue operations, where 
the queue is composed of subarrays with a maximum size of n elements each.
"""

import logging
from collections import deque
from typing import Optional

class QueueNode:
    def __init__(self, max_queue_node_size: int, next_node: Optional['QueueNode'] = None):
        # check if provided queue size is valid
        if not isinstance(max_queue_node_size, int) or max_queue_node_size < 1:     # if TypeError or ValueError
            default_queue_size = 5
            logging.error(f"Max queue node size must be an integer greater than 0. Defaulting to {default_queue_size}")
            self.max_q_size = default_queue_size
        else:
            self.max_q_size = max_queue_node_size
        self.next_node = next_node
        self.q = deque()

    def size(self) -> int:
        return len(self.q)

    def is_full(self) -> bool:
        return self.size() == self.max_q_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def add(self, val) -> bool:
        if self.is_full():
            return False
        self.q.append(val)
        return True

    def remove(self):
        if self.is_empty():
            raise IndexError("Index Error. Trying to remove from empty queue.")
        else:
            return self.q.popleft()

class UnlimitedQueue:
    def __init__(self, subarray_size: int):
        self.subarray_size = subarray_size
        self.curr_node = QueueNode(self.subarray_size)
        self.total_elements = 0
        self.unlimited_queue_head = self.curr_node

    def size(self) -> int:
        return self.total_elements

    def enqueue(self, val) -> bool:
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
        if self.size() == 0:
            raise IndexError("Index Error. Trying to remove from empty queue.")

        if self.unlimited_queue_head.is_empty() and self.unlimited_queue_head.next_node:
            # detach head node as it’s empty
            temp = self.unlimited_queue_head.next_node
            self.unlimited_queue_head.next_node = None
            self.unlimited_queue_head = temp
        
        self.total_elements -= 1
        # attempt to remove element from node
        return self.unlimited_queue_head.remove()

# testing
if __name__ == "__main__":
    uq = UnlimitedQueue(5)
        
    for i in range(1, 16):
        uq.enqueue(i)

    for _ in range(16):
        try:
            print(uq.dequeue())
        except IndexError as e:
            print(e)

    uq.enqueue(21)
            
    for i in range(0, 4):
        uq.enqueue(i)
        
    for _ in range(7):
        try:
            print(uq.dequeue())
        except IndexError as ex:
            print(ex)
