#!/usr/bin/env pypy3

import sys

pats, desired = sys.stdin.read().strip().split('\n\n')
pats = pats.split(', ')
desired = desired.split('\n')

# counting problem, == dp
def count(goal):
  dp = [0]*(len(goal)+1)
  dp[0] = 1
  for end in range(1, len(goal)+1):
    for cand in pats:
      start = end - len(cand)
      if start < 0:
        continue
      if goal[start:end] == cand:
        dp[end] += dp[start]
  return dp[len(goal)]

def part1():
  tot = 0
  for goal in desired:
    if count(goal):
      tot += 1
  return tot

def part2():
  tot = 0
  for goal in desired:
      tot += count(goal)
  return tot

print(part1())
print(part2())

#exit(1) # remove to run on data.in
