#!/usr/bin/env pypy3

import sys

data = sys.stdin.read().strip()
gridd, actions = data.split('\n\n')
gridd = gridd.split('\n')

walls = set()
init_boxes = set()
robot = None
for y, line in enumerate(gridd):
  for x, ch in enumerate(line):
    if ch == '#':
      walls.add((y,x))
    if ch == 'O':
      init_boxes.add((y,x))
    if ch == '@':
      robot = (y, x)

def step(boxes, robot, action):
  dx, dy = 0, 0
  if action == '<':
    dx = -1
  elif action == '>':
    dx = 1
  elif action == 'v':
    dy = 1
  elif action == '^':
    dy = -1
  else:
    return robot

  ry, rx = robot
  t = (ry + dy, rx + dx)
  if t in walls:
    return robot
  if not t in boxes:
    return t

  t2 = t
  while t2 in boxes:
    t2 = (t2[0] + dy, t2[1] + dx)
  if t2 in walls:
    return robot
  boxes.remove(t)
  boxes.add(t2)
  return t

def part1():
  rloc = robot
  boxes = set(s for s in init_boxes)
  for a in actions:
    rloc = step(boxes, rloc, a)
  return sum(100*y + x for (y, x) in boxes)

walls2 = set()
init_boxes2 = set()
robot2 = None
for y, line in enumerate(gridd):
  line = line.replace('#', '##').replace('.', '..').replace('O', 'O.').replace('@', '@.')
  for x, ch in enumerate(line):
    if ch == '#':
      walls2.add((y,x))
    if ch == 'O':
      init_boxes2.add((y,x))
    if ch == '@':
      robot2 = (y, x)

def has_box(boxes, loc):
  y, x = loc
  return loc in boxes or (y, x-1) in boxes

def box_origin(boxes, loc):
  y, x = loc
  if loc in boxes:
    return loc
  if (y, x-1) in boxes:
    return (y, x-1)

def box_locs(boxes, loc):
  assert(has_box(boxes, loc))
  y, x = box_origin(boxes, loc)
  return [(y, x), (y, x+1)]

def try_move(boxes, loc, dy, dx):
  assert(has_box(boxes, loc))
  y, x = loc
  cur_borigs = [box_origin(boxes, loc)]
  touched = set()
  while cur_borigs:
    nxt = []
    for borig in cur_borigs:
      touched.add(borig)
      if dy != 0:
        for (by, bx) in box_locs(boxes, borig):
          nloc = (by+dy, bx+dx)
          if nloc in walls2:
            return False
          if has_box(boxes, nloc):
            nxt.append(box_origin(boxes, nloc))
      if dx == -1:
        y, x = borig
        nloc = (y, x-1)
        if nloc in walls2:
          return False
        if (y, x-2) in boxes:
          nxt.append((y, x-2))
      if dx == 1:
        y, x = borig
        nloc = (y, x+2)
        if nloc in walls2:
          return False
        if (y, x+2) in boxes:
          nxt.append((y, x+2))
    cur_borigs = nxt
  boxes -= touched
  for (y, x) in touched:
    boxes.add((y+dy, x+dx))
  return True

def step2(boxes, robot, action):
  dx, dy = 0, 0
  if action == '<':
    dx = -1
  elif action == '>':
    dx = 1
  elif action == 'v':
    dy = 1
  elif action == '^':
    dy = -1
  else:
    return robot

  ry, rx = robot
  t = (ry + dy, rx + dx)
  if t in walls2:
    return robot
  if not has_box(boxes, t):
    return t

  if try_move(boxes, t, dy, dx):
    return t
  else:
    return robot


def pp(boxes, robot):
  lines = [['.']*len(gridd[0])*2 for _ in range(len(gridd))]
  for (y, x) in walls2:
    lines[y][x] = '#'
  for (y, x) in boxes:
    lines[y][x] = '['
    lines[y][x+1] = ']'
  lines[robot[0]][robot[1]] = '@'
  for line in lines:
    print(''.join(line))
  print()

def part2():
  rloc = robot2
  boxes = set(s for s in init_boxes2)
  for a in actions:
    rloc = step2(boxes, rloc, a)
  return sum(100*y + x for (y, x) in boxes)

print(part1())
print(part2())
