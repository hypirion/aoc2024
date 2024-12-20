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

def count_savings(steps, w):
  wy, wx = w
  # multiple? in theory..
  improvement = 0
  ret = []
  for dy, dx in moves:
    prev = wy + dy, wx + dx
    if prev in steps:
      prev_n = steps[prev]
      nxt = wy - dy, wx - dx
      if nxt in steps:
        nxt_n = steps[nxt]
        if 0 < nxt_n - prev_n - 2:
          # more than one?
          ret.append(nxt_n - prev_n -2)
  return ret

def on_border(wz):
  wy, wx = wz
  return wy == 0 or wy == h-1 or wx == 0 or wx == w-1

# 2 picos, but no 2 wall skip example??
# must move in same loc apparently

to_count = 100

def part1():
  steps = bfs(walls, start, goal)
  initial = steps[goal]
  #  res = Counter()
  #  for w in walls:
  #    if on_border(w):
  #      continue
  #    wy, wx = w
  #    walls.discard(w)
  #    stepss = bfs(walls, start, goal)[goal]
  #    if initial-stepss:
  #      res[initial-stepss] += 1
  #    for dy, dx in moves:
  #      # todo
  #      continue
  #      w2 = wy + dy, wx + dx
  #      has_wall = w2 in walls
  #      walls.discard(w2)
  #      stepss = bfs(walls, start, goal)[goal]
  #      res[initial-stepss] += 1
  #
  #      if has_wall:
  #        walls.add(w2)
  #    walls.add(w)
  #
  res = Counter()
  for w in walls:
    for saving in count_savings(steps, w):
      res[saving] += 1

  tot = 0
  for k, v in res.items():
    if to_count <= k:
      tot += v

  return tot

def count_savings2(steps, start, n):
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

def part2():
  steps = bfs(walls, start, goal)
  res = Counter()
  for loc in steps.keys():
    for saving in count_savings2(steps, loc, 19):
      res[saving] += 1

  tot = 0
  for k, v in res.items():
    if to_count <= k:
      tot += v

  return tot

to_count = 100

print(part1())
print(part2())

#exit(1) # remove to run on data.in

