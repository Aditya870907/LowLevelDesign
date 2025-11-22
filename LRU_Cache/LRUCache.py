from typing import Generic, Optional, TypeVar, Dict
import threading
from DoublyLinkedList import DoublyLinkedList
from node import Node

K = TypeVar('K')
V = TypeVar('V')

class LRUCache(Generic[K,V]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: Dict[K, Node[K,V]] = {}
        self.dll: DoublyLinkedList[K,V] = DoublyLinkedList()
        self.lock = threading.Lock()

    def get(self, key: K) -> Optional[V]:
        with self.lock:
            if key not in self.map:
                return None
            node = self.map[key]
            self.dll.move_to_front(node)
            return node.value
    
    def put(self, key: K, value: V) -> None:
        with self.lock:
            if key in self.map:
                node = self.map[key]
                self.dll.move_to_front(node)
            else:
                if len(self.map) >= self.capacity:
                    last_node = self.dll.remove_last()
                    if last_node:
                        del self.map[last_node.key]
                new_node = Node(key, value)
                self.dll.addFirst(new_node)
                self.map[key] = new_node
    
    def remove(self, key: K) -> None:
        with self.lock:
            if key in self.map:
                node = self.map[key]
                self.dll.remove(node)
                del self.map[key]
