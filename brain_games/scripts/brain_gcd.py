#!/usr/bin/env python3
"""Brain GCD game."""

from brain_games import gcd_cli

SUCCESS_TO_WIN = 3


def main():
    gcd_cli.start_game(SUCCESS_TO_WIN)


if __name__ == '__main__':
    main()
