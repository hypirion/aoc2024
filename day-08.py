#!/usr/bin/env pypy3

import sys
from collections import defaultdict
import itertools

lines = sys.stdin.read().strip().split('\n')

h = len(lines)
w = len(lines[0])

node_locs = defaultdict(lambda: [])
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
      if ch != '.':
        node_locs[ch].append((y, x))

def antinodes(pts):
  s = set()
  for (y1, x1), (y2, x2) in itertools.permutations(pts, 2):
    y3, x3 = 2*y1-y2, 2*x1-x2
    if 0 <= y3 < h and 0 <= x3 < w:
      s.add((y3, x3))
  return s

def part1():
  s = set()
  for ch, locs in node_locs.items():
    s |= antinodes(locs)
  return len(s)

def harmonic_antinodes(pts):
  s = set()
  for (y1, x1), (y2, x2) in itertools.permutations(pts, 2):
    dy, dx = y1-y2, x1-x2
    i = 0
    while True:
      y3, x3 = y1+dy*i, x1+dx*i
      if 0 <= y3 < h and 0 <= x3 < w:
        s.add((y3, x3))
        i += 1
      else:
        break
  return s

def part2():
  s = set()
  for ch, locs in node_locs.items():
    s |= harmonic_antinodes(locs)
  return len(s)

print(part1())
print(part2())
