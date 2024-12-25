#!/usr/bin/env pypy3

import sys

schems = sys.stdin.read().strip().split('\n\n')

def tpose(M):
  return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

keys = []
locks = []
for el in schems:
  lines = el.split('\n')
  is_lock = lines[0] == "#####"
  if is_lock:
    locks.append(tuple(x.count("#") - 1 for x in tpose(lines)))
  else:
    keys.append(tuple(x.count("#") - 1 for x in tpose(lines)))

def overlaps(key, lock):
  for l, k in zip(lock, key):
    if 5 < k + l:
      return True
  return False

def part1():
  tot = 0
  for lock in locks:
    for key in keys:
      if not overlaps(key, lock):
        tot += 1
  return tot

print(part1())

#exit(1) # remove to run on data.in
