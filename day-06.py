#!/usr/bin/env pypy3

import sys

allin = sys.stdin.read().strip().split('\n')

blocks = set()
gloc = None
for y, line in enumerate(allin):
  for x, ch in enumerate(line.strip()):
    if ch == '#':
      blocks.add((y,x))
    if ch == '^':
      gloc = (y, x)

blocks = frozenset(blocks)
print(len(blocks))

w = len(allin[0])
h = len(allin)

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def locs_used(blocks):
  locs = set()
  cur = gloc
  move_idx = 0
  while 0 <= cur[0] < h and 0 <= cur[1] < w:
    locs.add(cur)
    gy, gx = cur
    dy, dx = moves[move_idx%4]
    while (gy+dy, gx+dx) in blocks:
      move_idx += 1
      dy, dx = moves[move_idx%4]
    cur = (gy+dy, gx+dx)
  return locs

def part1():
  return len(locs_used(blocks))


def is_looping(blocks):
  locs = set()
  cur = gloc
  move_idx = 0
  while 0 <= cur[0] < h and 0 <= cur[1] < w:
    if (cur, move_idx) in locs:
      return True
    locs.add((cur, move_idx))
    gy, gx = cur
    dy, dx = moves[move_idx]
    while (gy+dy, gx+dx) in blocks:
      move_idx = (move_idx + 1)%4
      dy, dx = moves[move_idx]
    cur = (gy+dy, gx+dx)
  return False

def part2():
  options = locs_used(blocks) - frozenset([gloc])
  workable = 0
  return sum(is_looping(blocks | frozenset([opt])) for opt in options)

print(part1())
print(part2())
