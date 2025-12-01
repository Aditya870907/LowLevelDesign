from abc import ABC, abstractmethod
class HashStrategy(ABC):
    @abstractmethod
    def hash(self, data: str) -> int:
        pass