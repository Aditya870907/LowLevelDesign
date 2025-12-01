from .bloom_filter import BloomFilter
from hashing.strategy import HashStrategy

class Builder:
    def __init__(self):
        self.bit_set_size = 0
        self.num_hash_functions = 0
        self.strategies = None

    def with_bit_set_size(self, bit_set_size: int):
        if bit_set_size <= 0:
            raise ValueError("Bit set size must be greater than 0")
        self.bit_set_size = bit_set_size
        return self
    
    def with_num_hash_functions(self, num_hash_functions: int):
        if num_hash_functions <= 0:
            raise ValueError("Number of hash functions must be greater than 0")
        self.num_hash_functions = num_hash_functions
        return self
    
    def with_hash_strategies(self, strategies: list[HashStrategy]):
        if not strategies:
            raise ValueError("Hash strategies must be provided")
        self.strategies = strategies
        return self
    
    def build(self):
        if self.bit_set_size == 0 or self.num_hash_functions == 0 or self.strategies is None:
            raise ValueError("Bit set size, number of hash functions, and hash strategies must be provided")
        
        if len(self.strategies) != self.num_hash_functions:
            raise ValueError(
                f"Number of hash strategies ({len(self.strategies)})"
                f"must match the number of hash functions ({self.num_hash_functions})"
            )

        print(f"Creating Bloom Filter with specified parameters:"
        f"Bit set size: {self.bit_set_size}\n"
        f"Number of hash functions: {self.num_hash_functions}"
        )

        return BloomFilter(self.bit_set_size, self.num_hash_functions, self.strategies)