#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
# Create a parent class for all the Players in the game called Players.
# Create attributes for the players class( such as score, move)
# Create subclasses which will have their own attributes, plus the
# parent class attributes.
# HumanPlayer , ComputerPlayer, ReflectPlayer, CyclePlayer,
# Game
# HumanPlayer allows the user to input a move in order to play.
# ComputerPlayer used random to select a move for the computer.
# ReflectPlayer learns the computer's move, so that it doesn't return the
# #same move in the next round.
# CyclePlayer learns the human move it doesn't return the same
# #move in the previous round.

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    score = 0
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Let's play (rock/paper/scissors): ")
            if move.lower() in moves:
                return move.lower()
            else:
                print("Invalid move. Try again.")

    def show_moves(self, my_move, their_move):
        print(f"You played {my_move}.")
        print(f"Computer played {their_move}.")


class RandomPlayer(Player):
    def random_move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        return moves[(moves.index(self.my_move) + 1) % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0
        self.round = 10

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.show_moves(move1, move2)
        print(f"Player1: {move1}  Player2: {move2}")
        if beats(move1, move2):
            self.score1 += 1
            print("Player 1 wins!")
            print(f"Player1: {self.score1}, Player2: {self.score2}")
        elif beats(move2, move1):
            self.score2 += 1
            print("Player 2 wins!")
            print(f"Player1: {self.score1}, Player2: {self.score2}")
        else:
            print("Tie!")
            print(f"Player1: {self.score1}, Player2: {self.score2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        rounds_played = 0
        print("Start Game!")
        print("You will play against the computer.")
        while rounds_played < self.round:
            print(f"Round {rounds_played + 1}:")
            self.play_round()
            rounds_played += 1
        print("Game over!")
        print(f"Final score: Player1 {self.score1}, Player2 {self.score2}")


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
