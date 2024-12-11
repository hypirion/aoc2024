#!/usr/bin/env pypy3

import sys
from collections import namedtuple

data = list(map(int, sys.stdin.read().strip().split()))

def update_stone(s):
  if s == 0:
    return (1,)
  ss = str(s)
  if len(ss) % 2 == 0:
    sh = len(ss)//2
    return (int(ss[:sh]), int(ss[sh:]))
  return (s*2024,)

def dfs(mem, val, blinks):
  if blinks == 0:
    return 1
  if (val, blinks) in mem:
    return mem[(val, blinks)]
  sub = update_stone(val)
  tot = 0
  for el in sub:
    tot += dfs(mem, el, blinks-1)
  mem[(val, blinks)] = tot
  return tot

def run(n):
  mem = {}
  tot = 0
  for stone in data:
    tot += dfs(mem, stone, n)
  return tot

def part1():
  return run(25)

def part2():
  return run(75)


print(part1())
print(part2())

#exit(1) # remove to run on data.in
