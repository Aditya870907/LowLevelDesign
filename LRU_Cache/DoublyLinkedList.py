from typing import Generic, Optional, TypeVar
from node import Node

K = TypeVar('K')
V = TypeVar('V')

class DoublyLinkedList(Generic[K,V]):
    def __init__(self):
        self.head: Node[K,V] = Node(None, None)
        self.tail: Node[K,V] = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addFirst(self, node: Node[K,V]) -> None:
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def remove(self, node: Node[K,V]) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_front(self, node: Node[K,V]) -> None:
        self.remove(node)
        self.addFirst(node)
    
    def remove_last(self) -> Optional[Node[K,V]]:
        if self.tail.prev == self.head:
            return None
        node = self.tail.prev
        self.remove(node)
        return node
    