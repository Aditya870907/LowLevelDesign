from game import Game
from entities.snake import Snake
from entities.ladder import Ladder
from entities.dice import Dice

class SnakeAndLadderDemo:
    @staticmethod
    def main():
        board_entities = [
            Snake(10, 2),
            Snake(19, 7),
            Snake(28, 1),
            Snake(51, 6),
            Snake(63, 1),
            Ladder(17, 29),
            Ladder(36, 44),
            Ladder(54, 76),
            Ladder(62, 84),
        ]

        players = ["Player 1", "Player 2", "Player 3"]

        game = Game.Builder() \
        .set_board(100, board_entities) \
        .set_players(players) \
        .set_dice(Dice(1, 6)) \
        .build()

        game.play()

if __name__ == "__main__":
    SnakeAndLadderDemo.main()