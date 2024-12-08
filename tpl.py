#!/usr/bin/env pypy3

import sys

lines = sys.stdin.read().strip().split('\n')
for line in lines:
  print(line)

exit(1) # remove to run on data.in
