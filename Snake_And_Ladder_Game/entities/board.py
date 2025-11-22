from typing import List
from .board_entity import BoardEntity
class Board:
    def __init__(self, size: int, entities: List[BoardEntity]):
        self.size = size
        self.snake_and_ladder_map = {}

        for entity in entities:
            self.snake_and_ladder_map[entity.get_start()] = entity.get_end()
    
    def get_size(self) -> int:
        return self.size

    def get_final_position(self, position: int) -> int:
        return self.snake_and_ladder_map.get(position, position)