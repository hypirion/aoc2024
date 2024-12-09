#!/usr/bin/env pypy3

import sys

data = sys.stdin.read().strip()

used = []
p2 = []

for i, ch in enumerate(data):
  if i % 2 == 0:
    used.extend([i//2]*int(ch))
    p2.append((i//2, int(ch)))
  else:
    used.extend([None]*int(ch))
    p2.append((None, int(ch)))

def move_blks():
  disk = used[:]
  for i in range(len(disk)-1, -1, -1):
    if disk[i] is None:
      continue
    for j in range(i):
      if disk[j] is None:
        disk[j], disk[i] = disk[i], None
        break
  return disk


def part1():
  disk = move_blks()
  tot = 0
  for i, fid in enumerate(disk):
    if fid is not None:
      tot += i * fid
  return tot

def move_files():
  disk = p2[:]
  last_fid, _ = disk[-1]
  for fid in range(last_fid, -1, -1):
    for i in range(len(disk)):
      t_fid, flen = disk[i]
      if t_fid == fid:
        break

    # insert
    for j in range(i):
      jfid, empty_blocks = disk[j]
      if jfid is not None:
        continue
      if flen <= empty_blocks:
        remain = empty_blocks - flen
        disk[j] = disk[i]
        disk[i] = (None, flen)
        if remain:
          disk = disk[:j+1] + [(None, remain)] + disk[j+1:]
        break

  return disk

def expand_disk(disk):
  full = []
  for fid, flen in disk:
    full.extend([fid]*flen)
  return full

def pprint(disk):
  d = disk[:]
  for i in range(len(d)):
    if d[i] is None:
      d[i] = '.'
  print(''.join(map(str, d)))


def part2():
  disk = expand_disk(move_files())
  tot = 0
  for i, fid in enumerate(disk):
    if fid is not None:
      tot += i * fid
  return tot

print(part1())
print(part2())

#exit(1) # remove to run on data.in
