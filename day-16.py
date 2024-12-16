#!/usr/bin/env pypy3

import sys
from heapq import *
from collections import defaultdict

data = sys.stdin.read().strip()
grid = data.split('\n')

walls = set()
start, goal = None, None
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def rot90s(delta):
  dy, dx = delta
  return [(-dx, -dy), (dx, dy)] #?

for y, line in enumerate(grid):
  for x, ch in enumerate(line):
    if ch == '#':
      walls.add((y,x))
    if ch == 'S':
      start =(y,x)
    if ch == 'E':
      goal = (y, x)

def backtrack(prevs, goal):
  to_check = [(goal, delta) for delta in moves]
  seen = set()
  while to_check:
    cur = to_check.pop()
    if cur in seen:
      continue
    seen.add(cur)
    to_check.extend(list(prevs[cur]))

  locs = set(loc for loc, _ in seen)
  return locs

def dijkstra(start, goal):
  seen = defaultdict(lambda: 1e80)
  prevs = defaultdict(set)
  fst = (start, (0, 1))
  heap = [(0, fst, None)]
  best = float('Inf')

  while heap:
    cost, cur, prev = heappop(heap)
    loc, delta = cur
    if best < cost:
      break
    if seen[cur] < cost:
      continue
    if seen[cur] == cost and prev:
      prevs[cur].add(prev)
      continue
    if loc == goal:
      best = cost
      prevs[cur].add(prev)
      continue

    seen[cur] = cost
    if prev:
      prevs[cur].add(prev)

    y, x = loc
    dy, dx = delta
    nloc = (y+dy, x+dx)
    if nloc not in walls:
      heappush(heap, (cost+1, (nloc, delta), cur))
    for ndelta in rot90s(delta):
      heappush(heap, (cost+1000, (loc, ndelta), cur))

  return best, backtrack(prevs, goal)

best, tiles = dijkstra(start, goal)
print(best)
print(len(tiles))

# for y, line in enumerate(grid):
#   l = list(line)
#   for x in range(len(l)):
#     if (y, x) in tiles:
#       l[x] = 'O'
#   print(''.join(l))

#exit(1) # remove to run on data.in
