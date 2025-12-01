from hashing.strategy import HashStrategy
from bitarray import bitarray
class BloomFilter:
    def __init__(self, bit_set_size: int, num_hash_functions: int, strategies: list[HashStrategy]):
        self.bit_set_size = bit_set_size
        self.num_hash_functions = num_hash_functions
        self.hash_strategies = strategies
        self.bit_set = bitarray(bit_set_size)
        self.bit_set.setall(0)


    def add(self, item: str):
        for i in range(self.num_hash_functions):
            hash_value = self.hash_strategies[i].hash(item)
            index = abs(hash_value) % self.bit_set_size
            self.bit_set[index] = 1

    def might_contain(self, item: str) -> bool:
        for i in range(self.num_hash_functions):
            hash_value = self.hash_strategies[i].hash(item)
            index = abs(hash_value) % self.bit_set_size
            if not self.bit_set[index]:
                return False # Definitely not in the set
        return True # Probably in the set
    