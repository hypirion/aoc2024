#!/usr/bin/env pypy3

import sys,re
from collections import Counter

h, w = 7, 11

class Machine:
  def __init__(self, px, py, vx, vy):
    self.px = px
    self.py = py
    self.vx = vx
    self.vy = vy

  def step(self):
    return Machine((self.px + self.vx)%w, (self.py + self.vy)%h, self.vx, self.vy)

lines = sys.stdin.read().strip().split('\n')
robos = []
for line in lines:
  robos.append(Machine(*map(int,re.findall(r'(-?\d+)', line))))

if 15 < len(lines):
  h, w = 103, 101

def step(n, robos):
  for i in range(n):
    robos = [robo.step() for robo in robos]
  return robos

def pp(robos):
  grid = [['.']*w for _ in range(h)]

  locs = Counter((r.py, r.px) for r in robos)
  for (y, x), cnt in locs.items():
    grid[y][x] = str(cnt)

  for line in grid:
    print(''.join(line))

def quadrants(robos):
  locs = Counter((r.py, r.px) for r in robos)
  c = Counter()
  for (y, x), cnt in locs.items():
    if y == h//2 or x == w//2:
      continue
    c[(y < h//2, x < w//2)] += cnt
  return c

def part1():
  rs = step(100, robos)
  c = quadrants(rs)
  tot = 1
  for v in c.values():
    tot *= v
  return tot

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_xmas_tree(rs):
  locs = set((r.py, r.px) for r in rs)
  best = 0
  all_seen = set()
  for r in locs:
    if r in all_seen:
      continue
    seen = set()
    cur = [r]
    while cur:
      nxt = []
      for (y, x) in cur:
        seen.add((y, x))
        for (dy, dx) in moves:
          ny, nx = y+dy, x+dx
          if (ny, nx) in locs and (ny, nx) not in seen:
            nxt.append((ny, nx))
      cur = nxt
    best = max(best, len(seen))
    all_seen |= seen
  return best

def part2():
  rs = robos
  num_steps = 0
  best = 0
  num_steps = 0
  for _ in range(10_000): # guesswork on the number
    rs = [robo.step() for robo in rs]
    num_steps += 1
    cur = is_xmas_tree(rs)
    if best < cur:
      best = cur
      best_steps = num_steps
  return best_steps




print(part1())
print(part2())

exit(1) # remove to run on data.in
