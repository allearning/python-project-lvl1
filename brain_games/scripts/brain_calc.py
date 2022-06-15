#!/usr/bin/env python3
"""Brain calc game."""

from brain_games import calc_cli

SUCCESS_TO_WIN = 3


def main():
    calc_cli.start_game(SUCCESS_TO_WIN)


if __name__ == '__main__':
    main()
