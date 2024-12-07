#!/usr/bin/env pypy3

import sys, math

reports = []

for line in sys.stdin:
  reports.append(list(map(int, line.strip().split())))

def safe_report(xs):
  s = math.copysign(1, xs[0]-xs[1])
  for i in range(1, len(xs)):
    delta = xs[i-1] - xs[i]
    if not (1 <= abs(delta) <= 3) or s != math.copysign(1, delta):
      return False
  return True

def problem_damp_safe_report(xs):
  for i in range(len(xs)):
    fixed = xs[:i] + xs[i+1:]
    if safe_report(fixed):
      return True
  return False

def part1():
  return sum(safe_report(r) for r in reports)

def part2():
  return sum(problem_damp_safe_report(r) for r in reports)

print(part1())
print(part2())

