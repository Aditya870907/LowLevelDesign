from .board_entity import BoardEntity
class Ladder(BoardEntity):
    def __init__(self, start: int, end: int):
        super().__init__(start, end)

        if start >= end:
            raise ValueError("Start base must be lower position than end top")