# File: generate.py
# Author: Michael Huelsman
# Created On: 20 May 2026
# Purpose:
#   Generates a number of random points for creating an
#   instance of the convex hull problem.

import argparse
from random import randint

def random_point(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return randint(x[0], x[1]), randint(y[0], y[1])

def main(args):
    points = set()
    while len(points) != args.n:
        points.add(random_point(args.x, args.y))
    for point in points:
        print(f"point({point[0]},{point[1]}).")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Convex Hull Instance Generator")
    parser.add_argument('-n', default=10, type=int, help="The number of points to create.")
    parser.add_argument('-x', nargs=2, default=(-10, 10), type=int, help="The lower and upper bounds for x values.")
    parser.add_argument('-y', nargs=2, default=(-10, 10), type=int, help="The lower and upper bounds for y values.")
    args = parser.parse_args()
    args.x = tuple(sorted(args.x))
    args.y = tuple(sorted(args.y))
    main(args)
