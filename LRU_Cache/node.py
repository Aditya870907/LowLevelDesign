from typing import Generic, Optional, TypeVar

K = TypeVar('K')
V = TypeVar('V')

class Node(Generic[K,V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value
        self.prev: Optional['Node[K,V]'] = None
        self.next: Optional['Node[K,V]'] = None
        