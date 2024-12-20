#!/usr/bin/env pypy3

import sys
from collections import Counter

grid = sys.stdin.read().strip().split('\n')

h, w = len(grid), len(grid[0])

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

walls = set()
for y, line in enumerate(grid):
  for x, ch in enumerate(line):
    if ch == 'S':
      start = (y, x)
    if ch == 'E':
      goal = (y, x)
    if ch == '#':
      walls.add((y, x))

def bfs(w, s, g):
  dist = {}
  steps = 0
  cur = [s]
  while cur:
    nxt = []
    for loc in cur:
      y, x = loc
      if loc in dist:
        continue
      dist[loc] = steps
      if loc == g:
        return dist
      for dy, dx in moves:
        n = y + dy, x + dx
        if n not in w and n not in dist:
          nxt.append(n)
    cur = nxt
    steps += 1
  return dist

def count_savings(steps, start, n):
  start_n = steps[start]
  cur = [start]
  seen = set(cur)
  ret = []
  for picos in range(n+1):
    nxt = []
    for p in cur:
      py, px = p
      for dy, dx in moves:
        n = py+dy, px+dx
        if n in seen:
          continue
        seen.add(n)
        nxt.append(n)
        if n in steps:
          n_n = steps[n]
          savings = n_n - start_n - picos - 1
          if 0 < savings:
            ret.append(savings)
    cur = nxt
  return ret

def solve(cheat_dist):
  steps = bfs(walls, start, goal)
  res = Counter()
  for loc in steps.keys():
    for saving in count_savings(steps, loc, cheat_dist-1):
      res[saving] += 1

  tot = 0
  for k, v in res.items():
    if to_count <= k:
      tot += v

  return tot

to_count = 100

def part1():
  return(solve(2))

def part2():
  return(solve(20))

print(part1())
print(part2())

#exit(1) # remove to run on data.in

