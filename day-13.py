#!/usr/bin/env pypy3

import sys
import re
from collections import namedtuple
import math

Machine = namedtuple('Machine', ['a', 'b', 'loc'])

machines = []
fy = 0
fx = 1

grps = sys.stdin.read().strip().split('\n\n')
for grp in grps:
  lines = grp.split('\n')

  ax, ay = map(int, re.findall(r'(\d+)', lines[0]))
  bx, by = map(int, re.findall(r'(\d+)', lines[1]))
  tx, ty = map(int, re.findall(r'(\d+)', lines[2]))
  machines.append(Machine((ay, ax), (by, bx), (ty, tx)))

# jesus, just linear eq. just finish this atm
def solve(m, cutoff):
  def _as():
    y, x, cost, presses = 0, 0, 0, 0
    while y < m.loc[fy] and x < m.loc[fx] and presses <= cutoff:
      yield((y, x, cost))
      y += m.a[fy]
      x += m.a[fx]
      cost += 3
      presses += 1
  def rec_b(y, x, cost):
    presses = 0
    while y <= m.loc[fy] and x <= m.loc[fx] and presses <= cutoff:
      if (y, x) == m.loc:
        return cost
      if m.loc[fy] < y or m.loc[fx] < x:
        return float('Inf')
      y += m.b[fy]
      x += m.b[fx]
      cost += 1
      presses += 1
    return float('Inf')

  best = float('Inf')
  for (y, x, cost) in _as():
    best = min(best, rec_b(y, x, cost))
  return best

def part1():
  tot = 0
  for m in machines:
    res = solve(m, 100)
    if not math.isinf(res):
      tot += res
  return tot

def solve_linear(m):
  amul = (m.loc[fx]*m.b[fy]-m.loc[fy]*m.b[fx])/(m.b[fy]*m.a[fx]-m.b[fx]*m.a[fy])
  bmul = (m.loc[fx]*m.a[fy]-m.loc[fy]*m.a[fx])/(m.b[fx]*m.a[fy]-m.b[fy]*m.a[fx])
  if 0 < amul and 0 < bmul and int(amul) == amul and int(bmul) == bmul:
    return int(amul*3)+int(bmul)
  return 0


def part2():
  tot = 0
  for m in machines:
    m2 = Machine(m.a, m.b, tuple(v+10000000000000 for v in m.loc))
    tot += solve_linear(m2)
  return tot


print(part1())
print(part2())

#exit(1) # remove to run on data.in
