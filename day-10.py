#!/usr/bin/env pypy3

import sys

raw = sys.stdin.read().strip().split('\n')

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = []
def intx(v):
  try:
    return int(v)
  except Exception:
    return None

for line in raw:
  grid.append(list(map(intx, line)))

h, w = len(grid), len(grid[0])

def loc(y, x):
  if y < 0 or x < 0:
    return None
  try:
    return grid[y][x]
  except Exception:
    return None

def bfs1(start):
  cur = set([start])
  for i in range(9):
    nxt = set()
    for y, x in list(cur):
      if loc(y, x) != i:
        continue
      for ny, nx in list((y+dy, x+dx) for dy, dx in moves):
        nxt.add((ny, nx))
    cur = nxt
  return sum(loc(y, x) == 9 for y, x in list(cur))


def part1():
  tot = 0
  for y in range(h):
    for x in range(w):
      tot += bfs1((y, x))
  return tot

def bfs2(start):
  cur = [start]
  for i in range(9):
    nxt = []
    for y, x in list(cur):
      if loc(y, x) != i:
        continue
      for ny, nx in list((y+dy, x+dx) for dy, dx in moves):
        nxt.append((ny, nx))
    cur = nxt
  return sum(loc(y, x) == 9 for y, x in cur)

def part2():
  tot = 0
  for y in range(h):
    for x in range(w):
      tot += bfs2((y, x))
  return tot

print(part1())
print(part2())

#exit(1) # remove to run on data.in
