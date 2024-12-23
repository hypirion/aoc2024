#!/usr/bin/env pypy3

import sys
from collections import defaultdict

secrets = list(map(int,sys.stdin.read().strip().split('\n')))

def rng(val):
  v1 = val << 6
  val = (val ^ v1) % 16777216
  v2 = val >> 5
  val = (val ^ v2) % 16777216
  v3 = val << 11
  val = (val ^ v3) % 16777216
  return val

def bananas(val):
  return val % 10

def part1():
  tot = 0
  for sec in secrets:
    cur = sec
    for i in range(2000):
      cur = rng(cur)
    tot += cur
  return tot

def banana_mapping(seed):
  deltas = []
  cur = seed
  m = {}
  for i in range(2000):
    nxt = rng(cur)
    delta = bananas(nxt) - bananas(cur)
    deltas.append(delta)
    if len(deltas) == 4:
      d = tuple(deltas)
      if d not in m:
        m[tuple(deltas)] = bananas(nxt)
      deltas.pop(0)
    cur = nxt
  return m

def part2():
  m = defaultdict(int)
  for bm in map(banana_mapping, secrets):
    for k, v in bm.items():
      m[k] += v
  best = None
  best_cnt = 0
  for k, v in m.items():
    if best_cnt < v:
      best_cnt = v
      best = k
  return best_cnt

print(part1())
print(part2())
