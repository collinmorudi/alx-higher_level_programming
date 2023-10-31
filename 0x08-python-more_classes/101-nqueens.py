#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking algorithm
"""


def can_attack(lst_queens, n_queen):
    """ Determines if the queens can or can't attack each other

    Args:
        lst_queens: list with indexes of the queens
        n_queen: queen number

    Return:
        True: when queens can't attack each other
        False: when some of the queens can attack
    """

    for i in range(n_queen):

        if lst_queens[i] == lst_queens[n_queen]:
            return False

        if abs(lst_queens[i] - lst_queens[n_queen]) == abs(i - n_queen):
            return False

    return True


def print_result(lst_queens, n_queen):
    """ Method that prints the list with the Queens positions
    Args:
        lst_queens: list with indexes of the queens
        n_queen: queen number
    """

    res = []

    for i in range(n_queen):
        res.append([i, lst_queens[i]])

    print(res)


def Queen(lst_queens, n_queen):
    """ Recursive method that executes the Backtracking algorithm
    Args:
        lst_queens: list with indexes of the queens
        n_queen: queen number
    """

    if n_queen is len(lst_queens):
        print_result(lst_queens, n_queen)
        return

    lst_queens[n_queen] = -1

    while ((lst_queens[n_queen] < len(lst_queens) - 1)):

        lst_queens[n_queen] += 1

        if can_attack(lst_queens, n_queen) is True:

            if n_queen is not len(lst_queens):
                Queen(lst_queens, n_queen + 1)


def solve(size):
    """ Invokes the Backtracking algorithm
    Args:
        size: size of the chessboard
    """

    lst_queens = [-1 for i in range(size)]

    Queen(lst_queens, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(size)
