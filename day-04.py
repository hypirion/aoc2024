#!/usr/bin/env pypy3

import sys
import itertools

grid = [line.strip() for line in sys.stdin]

h, w = len(grid), len(grid[0])

def scan1(target):
  tot = 0
  for y in range(h):
    for x in range (w):
      for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
          if dy == dx == 0:
            continue
          matches = 0
          for i, ch in enumerate(target):
            if y+dy*i < 0 or h <= y+dy*i or x+dx*i < 0 or w <= x+dx*i:
              break
            # print(y, x, dy, dx, i, ch, grid[y+dy*i][x+dx*i])
            if grid[y+dy*i][x+dx*i] == ch:
              matches += 1
            else:
              break
          # print('matches', matches)
          if matches == len(target):
            tot += 1
  return tot

def scan2(target):
  tot = 0
  for y in range(h):
    for x in range (w):
      dy, dx = 1, 1
      matches = 0
      for i, ch in enumerate(target):
        if y+dy*i < 0 or h <= y+dy*i or x+dx*i < 0 or w <= x+dx*i:
          break
        # print(y, x, dy, dx, i, ch, grid[y+dy*i][x+dx*i])
        if grid[y+dy*i][x+dx*i] == ch:
          matches += 1
        else:
          break
        # print('matches', matches)
      if matches == len(target):
        yield(y, x)

def crossup(y, x, target):
  dy, dx = -1, 1
  matches = 0
  for i, ch in enumerate(target):
    if y+dy*i < 0 or h <= y+dy*i or x+dx*i < 0 or w <= x+dx*i:
      break
    # print(y, x, dy, dx, i, ch, grid[y+dy*i][x+dx*i])
    if grid[y+dy*i][x+dx*i] == ch:
      matches += 1
    else:
      break
    # print('matches', matches)
  return matches == len(target)

def part2():
  tot = 0
  for (y, x) in itertools.chain(scan2('MAS'), scan2('SAM')):
    if crossup(y+2, x, 'MAS') or crossup(y+2, x, 'SAM'):
      tot += 1
  return tot
    

print(scan1('XMAS'))
print(part2())
