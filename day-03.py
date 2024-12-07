#!/usr/bin/env pypy3

import sys, re

data = sys.stdin.read().strip()

muls = re.findall(r'mul\((\d+),(\d+)\)', data)

tot = 0
for a, b in muls:
  tot += int(a)*int(b)

print(tot)

mulpp = re.findall(r"mul\((\d+),(\d+)\)|(do(n't)?)\(\)", data)

tot = 0
do_perform = True
for a, b, do, _ in mulpp:
  if do:
    do_perform = do == "do"
  if a and b and do_perform:
    tot += int(a)*int(b)

print(tot)
