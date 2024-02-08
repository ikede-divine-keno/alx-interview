#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem."""
import sys


def main():
    """ main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    col = set()
    posDiag = set()
    negDiag = set()
    res = []
    board = [["."] * N for i in range(N)]

    def solve_nqueens(r):
        """ solve n quuen issue, function to backtrack the solution"""
        if r == N:
            copy = [list(row) for row in board]  # Append each row as a list
            res.append(copy)
            return
        for c in range(N):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'

            solve_nqueens(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'

    solve_nqueens(0)
    rowcount = 0
    colcount = 0
    f = []
    for solution in res:
        for row in solution:
            for ele in row:
                if ele == 'Q':
                    f.append([rowcount, colcount])
                colcount += 1
            colcount = 0
            rowcount += 1
        print(f)
        f = []
        rowcount = 0


if __name__ == "__main__":
    """ main call"""
    main()
