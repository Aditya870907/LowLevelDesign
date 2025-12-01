from .strategy import HashStrategy
class DJB2HashStrategy(HashStrategy):
    def hash(self, data: str) -> int:
        hash_value = 5381
        for byte in data.encode('utf-8'):
            # hash = hash * 33 + c
            hash_value = ((hash_value << 5) + hash_value) + byte

        return hash_value