#!/usr/bin/env pypy3

import sys

grid = sys.stdin.read().strip().split('\n')

h, w = len(grid), len(grid[0])

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def loc(y, x):
  if y < 0 or x < 0:
    return None
  try:
    return grid[y][x]
  except Exception:
    return None

groups = []

def bfs(y, x):
  grp = set([(y, x)])
  val = grid[y][x]
  cur = [(y, x)]
  while cur:
    nxt = []
    for (y, x) in cur:
      for (dy, dx) in moves:
        ny, nx = y+dy, x+dx
        if loc(ny, nx) == val and (ny, nx) not in seen:
          seen.add((ny, nx))
          grp.add((ny, nx))
          nxt.append((ny, nx))
      cur = nxt
  return grp

def area(grp):
  return len(grp)

def perim(grp):
  tot = 0
  for (y, x) in grp:
    for (dy, dx) in moves:
      ny, nx = y+dy, x+dx
      if (ny, nx) not in grp:
        tot += 1
  return tot

plot_sides = moves

def sides(grp):
  sseen = set()
  ccs = 0
  for (y, x) in grp:
    for (dy, dx) in moves:
      if (y+dy, x+dx) in grp:
        continue
      # n = outside, d = outside "side"
      # find 'canonical' corner side
      cy, cx = y, x
      while (cy+dx, cx+dy) in grp and (cy+dy, cx+dx) not in grp:
          cy += dx
          cx += dy
      if (cy, cx, dy, dx) not in sseen:
        sseen.add((cy, cx, dy, dx))
        ccs += 1
  return ccs


seen = set()
part1 = 0
part2 = 0
for y in range(h):
  for x in range(w):
    if (y, x) in seen:
      continue
    grp = bfs(y, x)
    a, p, s = area(grp), perim(grp), sides(grp)
    part1 += a*p
    part2 += a*s

print(part1)
print(part2)
    
#exit(1) # remove to run on data.in
