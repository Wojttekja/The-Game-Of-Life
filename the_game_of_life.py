"""The game of life"""
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# path to save the boards
PATH = "boards"

os.system(f"rm -r {PATH}")
os.system(f"mkdir {PATH}")

# dimensions of the board
N = 8

# max limit of steps 
LIMIT = 200

def init_array(x: int):
    """Init x*x table""" 
    array = np.zeros(x*x)
    array[::2] = False
    array = array.reshape((x, x))
    return array


def start_stage(array, x: int):
    """fills the array randomly with True or False"""
    for i in range(x):
        for j in range(x):
            array[i, j] = random.choice([True, False])
    return array


def show(array, n: int, number: int, path: str) -> None:
    """Show board using pyplot"""
    rowcol = range(n)
    plt.matshow(array)
    plt.xticks(range(n), rowcol)
    plt.yticks(range(n), rowcol)
    plt.savefig(f"{path}/{number}.png")
    plt.close()


def how_many_live_neighbours(x: int, y: int, array, n: int) -> bool:
    global shifts
    result = 0
    for i in shifts:
        if array[(x-i[0])%n, (y-i[1])%n]:
            result += 1
    return result


def step(old, n):
    new = init_array(n)
    for x in range(n):
        for y in range(n):
            match how_many_live_neighbours(x, y, old, n):
                case 2:
                    new[x, y] = old[x, y]
                case 3:
                    new[x, y] = True
                case other:
                    new[x, y] = False
    return new

board = start_stage(init_array(N), N)

# how to shift index to find neighbours of a cell
shifts = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
shifts.remove((0, 0))

i = 0
show(board, N, i, PATH)
while True in board and i < LIMIT:
    board = step(board, N)
    i += 1
    show(board, N, i, PATH)
print(i)