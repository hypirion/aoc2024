#!/usr/bin/env pypy3

import sys
from collections import defaultdict
# import networkx as nx # couldn't get max_clique to work??
from functools import cache

lines = sys.stdin.read().strip().split('\n')
conns = defaultdict(set)
nodes = set()
for line in lines:
  a, b = line.split('-')
  nodes.add(a)
  nodes.add(b)
  conns[a].add(b)
  conns[b].add(a)

def directly_connected():
  opts = set()
  for root in nodes:
    for child1 in conns[root]:
      for child2 in conns[child1]:
        if child2 in conns[root]:
          opts.add(frozenset([root, child1, child2]))
  return opts


def part1():
  ts = 0
  for st in directly_connected():
    for x in st:
      if x[0] == 't':
        ts += 1
        break
  return ts

@cache
def clique_rec(st, n):
  best = st
  opts = conns[n]
  if st.issubset(opts):
    st |= frozenset([n])
    best = st
    for opt in opts:
      if opt in st:
        continue
      candidate = clique_rec(st, opt)
      if len(best) < len(candidate):
        best = candidate
  return best

def max_clique():
  best = frozenset()
  for n in nodes:
    candidate = clique_rec(frozenset(), n)
    if len(best) < len(candidate):
      best = candidate
  return best

def part2():
  return ','.join(sorted(max_clique()))

print(part1())
# time to kill the computer
print(part2())


#exit(1) # remove to run on data.in
