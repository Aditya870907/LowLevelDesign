from enums.game_status import GameStatus
from entities.board import Board
from entities.player import Player
from entities.dice import Dice
from entities.board_entity import BoardEntity
from typing import List
from collections import deque

class Game:
    class Builder:
        def __init__(self):
            self.board = None
            self.players = None
            self.dice = None

        def set_board(self, board_size: int, entities: List[BoardEntity]):
            self.board = Board(board_size, entities)
            return self
        
        def set_players(self, player_names: List[str]):
            self.players = deque()
            for name in player_names:
                self.players.append(Player(name))
            return self
        
        def set_dice(self, dice: Dice):
            self.dice = dice
            return self
        
        def build(self):
            if self.board is None or self.players is None or self.dice is None:
                raise ValueError("Board, players, and dice are required")
            return Game(self)
    
    def __init__(self, builder: 'Game.Builder'):
        self.board = builder.board
        self.players = deque(builder.players)
        self.dice = builder.dice
        self.status = GameStatus.NOT_STARTED
        self.winner = None

    def play(self) -> None:
        if len(self.players) < 2:
            print("At least 2 players are required to play the game")
            return
        self.status = GameStatus.RUNNING
        print(f"Game started with {len(self.players)} players")

        while self.status == GameStatus.RUNNING:
            current_player = self.players.popleft()
            self.take_turn(current_player)

            # If the game is not finished and player didn't hit 6, add the player back to the queue
            if self.status == GameStatus.RUNNING:
                self.players.append(current_player)
        
        print(f"Game finished. Winner is {self.winner.get_name()}")
    

    def take_turn(self, player: Player) -> None:
        roll = self.dice.roll()
        print(f"{player.get_name()} rolled a {roll}")

        current_position = player.get_position()
        new_position = current_position + roll

        if new_position > self.board.get_size():
            print(f"Oops, {player.get_name()} needs to land exactly on {self.board.get_size()}. Turn skipped.")
            return
        
        if new_position == self.board.get_size():
            self.winner = player
            self.status = GameStatus.FINISHED
            player.set_position(new_position)
            print(f"Congratulations! {player.get_name()} has won the game!")
            return
        
        final_position = self.board.get_final_position(new_position)

        if final_position > new_position:
            print(f"Wow! {player.get_name()} found a ladder 🪜 at {new_position} and climbed to {final_position}.")
        elif final_position < new_position:
            print(f"Oh no! {player.get_name()} was bitten by a snake 🐍 at {new_position} and slid down to {final_position}.")
        else:
            print(f"Nice! {player.get_name()} landed exactly on {final_position}.")

        player.set_position(final_position)

        if roll == 6:
            print(f"{player.get_name()} rolled a 6 and gets another turn!")
            self.take_turn(player)