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
  cur = [goal]
  seen = set()
  while cur:
    loc = cur.pop()
    if loc in seen:
      continue
    seen.add(loc)
    cur.extend(list(prevs[loc]))
  return seen

def dijkstra(start, goal):
  seen = defaultdict(lambda: 1e80)
  prevs = defaultdict(set)
  cur = [(0, start, (0, 1), start)]
  best = float('Inf')

  while cur:
    cost, loc, delta, prev = heappop(cur)
    if best < cost:
      break
    if seen[(loc, delta)] < cost:
      continue
    if seen[(loc, delta)] == cost and loc != prev:
      prevs[loc].add(prev)
      continue
    if loc == goal:
      best = cost
      prevs[loc].add(prev)
      continue

    seen[(loc, delta)] = cost
    if loc != prev:
      prevs[loc].add(prev)

    y, x = loc
    dy, dx = delta
    nloc = (y+dy, x+dx)
    if nloc not in walls:
      heappush(cur, (cost+1, nloc, delta, loc))
    for ndelta in rot90s(delta):
      heappush(cur, (cost+1000, loc, ndelta, loc))

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
