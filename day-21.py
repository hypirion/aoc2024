#!/usr/bin/env pypy3

import sys

from collections import namedtuple, defaultdict, Counter

codes = sys.stdin.read().strip().split('\n')

def mk_graph(lines):
  g = {}
  for y, line in enumerate(lines):
    for x, ch in enumerate(line):
      if ch == '_':
        continue
      g[(y, x)] = ch
      g[ch] = (y, x)
      # ew ^
  return g

numpad = mk_graph("789\n456\n123\n_0A".split())
dir_kb = mk_graph("_^A\n<v>".split())

moves = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1),
}

def find_paths(g, start_key, goal_key):
  start_loc = g[start_key]
  cur = [('', start_loc)]
  step = -1
  seen = defaultdict(lambda: 10000)
  paths = []
  while cur:
    nxt = []
    step += 1
    for (cur_path, loc) in cur:
      y, x = loc

      if seen[loc] < step:
        continue
      seen[loc] = step

      if g[loc] == goal_key:
        paths.append(cur_path+'A')
        continue
      for k, (dy, dx) in moves.items():
        n = y + dy, x + dx
        if n in g:
          nxt.append((cur_path + k,n))
    cur = nxt
  return paths

numpad_pairs = {}
for start in '0123456789A':
  for goal in '0123456789A':
    numpad_pairs[(start, goal)] = find_paths(numpad, start, goal)

dir_kb_pairs = {}
for start in '^<v>A':
  for goal in '^<v>A':
    dir_kb_pairs[(start, goal)] = find_paths(dir_kb, start, goal)

def numeric_part(code):
  return int(''.join(ch for ch in code if ch.isnumeric()))

def path_len(lt, path):
  cur = 'A'
  tot = 0
  for ch in path:
    tot += lt[(cur, ch)]
    cur = ch
  return tot

def expand0(path):
  cur = 'A'
  seq = []
  for ch in path:
    seq.append(numpad_pairs[(cur, ch)])
    cur = ch
  return seq

dp = []

m = {}
for (a, b), v in dir_kb_pairs.items():
  m[(a, b)] = len(v[0])

dp.append(m)
def more_dp():
  prev = dp[-1]
  m = {}
  for k, vs in dir_kb_pairs.items():
    best = float('Inf')
    for v in vs:
      best = min(best, path_len(prev, v))
    m[k] = best
  dp.append(m)

def solve(code, levels):
  while len(dp) <= levels:
    more_dp()
  m = dp[levels]
  tot = 0
  for alts in expand0(code):
    best = float('Inf')
    for alt in alts:
      best = min(best, path_len(m, alt))
    tot += best
  return tot

def run(level):
  n = level+1
  tot = 0
  for code in codes:
    tot += numeric_part(code) * solve(code, n-2)
  return tot

def part1():
  return run(2)

def part2():
  return run(25)

print(part1())
print(part2())

#exit(1) # remove to run on data.in
