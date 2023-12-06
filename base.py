#! /usr/bin/env python3

# Advent of Code
# https://adventofcode.com/2023
# Day

import argparse

from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='AoC 2023 Day XX')
    parser.add_argument('-t', '--test', help='use test data', action='store_true')
    args = parser.parse_args()
    return args

def parse_input(inpt):
    return


if __name__ == '__main__':
    args = parse_args()
    if args.test:
        in_file = Path('test.txt')
    else:
        in_file = Path('input.txt')
    puzzle_input = in_file.read_text(encoding='utf-8')

    print('Part 1:')

    print('Part 2:')
