#!/usr/bin/env pypy3

import sys

lines = sys.stdin.read().strip().split('\n')
corrupted = []
for line in lines:
  x, y = list(map(int, line.split(',')))
  corrupted.append((y, x))

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
if len(corrupted) < 1000:
  n = 12
  h, w = 7, 7
  goal = (6, 6)
else:
  n = 1024
  h, w = 71, 71
  goal = (70, 70)

def solve(num_corrupted):
  blocked = set(corrupted[:num_corrupted])
  cur = [(0, 0)]
  seen = set()
  for i in range(h*w):
    nxt = []
    for loc in cur:
      y, x = loc
      if loc in seen or y < 0 or h <= y or x < 0 or h <= x:
        continue
      if loc in blocked:
        continue
      if loc == goal:
        return i
      seen.add(loc)
      for (dy, dx) in moves:
        nxt.append((y+dy, x+dx))
    cur = nxt
  return None

def part1():
  return solve(n)

def pp():
  for y in range(h):
    l = ['.']*w
    for (cy, cx) in set(corrupted[:n]):
      if y == cy:
        l[cx] = '#'
    print(''.join(l))

def part2():
  for i in range(len(corrupted)):
    if solve(i+1) is None:
      y, x = corrupted[i]
      return ','.join(map(str, ((x, y))))


print(part1())
print(part2())
#exit(1) # remove to run on data.in
