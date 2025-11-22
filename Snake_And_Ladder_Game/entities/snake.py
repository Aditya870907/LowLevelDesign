from .board_entity import BoardEntity
class Snake(BoardEntity):
    def __init__(self, start: int, end: int):
        super().__init__(start, end)

        if start <= end:
            raise ValueError("Start head must be heigher position than end tail")