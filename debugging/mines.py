#!/usr/bin/python3

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample([(x, y) for x in range(width) for y in range(height)], mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.safe_cells = self.total_cells - mines

    def print_board(self, reveal=False):
        clear_screen()
        print("  " + " ".join(str(x) for x in range(self.width)))
        print(" +" + "--" * self.width + "+")

        for y in range(self.height):
            print(f"{y}|", end="")
            for x in range(self.width):
                if self.revealed[y][x] or reveal:
                    if (x, y) in self.mines:
                        print("*", end=" ")
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=" ")
                else:
                    print(".", end=" ")
            print("|")
        print(" +" + "--" * self.width + "+")

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return
        self.revealed[y][x] = True
        if (x, y) in self.mines:
            return False

        count = self.count_mines_nearby(x, y)
        if count == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def play(self):
        revealed_cells = 0
        while True:
            self.print_board()
            try:
                x, y = map(int, input("Enter x y coordinate (e.g., '3 4'): ").split())
                if not (0 <= x < self.width and 0 <= y < self.height):
                    raise ValueError("Coordinates out of bounds!")
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid coordinates.")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            revealed_cells = sum(self.revealed[y][x] for x in range(self.width) for y in range(self.height))

            if revealed_cells == self.safe_cells:
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
