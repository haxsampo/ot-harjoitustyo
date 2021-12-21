import heapq
from typing import Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional
T = TypeVar('T')

class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []

    def empty(self):
        '''
        Return:
        bool - based on whether elements is empty or not
        '''
        return not self.elements

    def put(self, item: T, priority: float):
        '''
        puts the given element in the heap, so that position is based on priority
        '''
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        '''
        return:
        '''
        return heapq.heappop(self.elements)[1]
