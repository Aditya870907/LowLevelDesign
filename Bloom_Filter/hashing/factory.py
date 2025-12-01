from enums.hash_type import HashType
from .djb2_strategy import DJB2HashStrategy
from .fnv1a_strategy import FNV1AHashStrategy
from .strategy import HashStrategy

class HashStrategyFactory:
    def create(hash_type: HashType) -> HashStrategy:
        if hash_type == HashType.FNV1A:
            return FNV1AHashStrategy()
        elif hash_type == HashType.DJB2:
            return DJB2HashStrategy()
        else:
            raise ValueError(f"Unsupported hash type: {hash_type}")