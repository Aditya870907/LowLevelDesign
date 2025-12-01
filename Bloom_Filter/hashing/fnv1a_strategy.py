from .strategy import HashStrategy
class FNV1AHashStrategy(HashStrategy):
    # FNV-1a 64-bit constants
    FNV_PRIME = 0x100000001b3
    FNV_OFFSET_BASIS = 0xcbf29ce484222325

    def hash(self, data: str) -> int:
        hash_value = self.FNV_OFFSET_BASIS
        for byte in data.encode('utf-8'):
            hash_value ^= byte
            hash_value *= self.FNV_PRIME
        return hash_value
        