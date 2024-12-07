#!/usr/bin/env pypy3

import sys
from collections import Counter

left, right = [], []

for line in sys.stdin:
    l, r = map(int, line.strip().split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

def part1():
  diff = 0
  for a, b in zip(left, right):
    diff += abs(a-b)
  return diff

def part2():
  rcount = Counter(right)
  similarity = 0
  for el in left:
    similarity += el * rcount[el]
  return similarity

print(part1())
print(part2())

