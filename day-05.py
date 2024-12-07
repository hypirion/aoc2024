#!/usr/bin/env pypy3

import sys
from collections import defaultdict

x, y = (v.strip() for v in sys.stdin.read().strip().split('\n\n'))

order_rules = [tuple(map(int, r.split('|'))) for r in x.split('\n')]

before_map = defaultdict(lambda: set())
for (before, after) in order_rules:
  before_map[after].add(before)

# implicit check: if all before have been seen, then they have been checked too

updates = [list(map(int, r.split(','))) for r in y.split('\n')]

def mid(update):
  return update[len(update)//2]

def correct_order(update):
  all_pages = set(update)
  seen = set()
  for page in update:
    seen.add(page)
    print_before = before_map[page] & all_pages
    if print_before - seen:
      return False
  return True

def fix(update):
  inserted = set()
  all_pages = set(update)
  new_order = []
  def insert(page):
    if page in inserted:
      return
    print_before = before_map[page] & all_pages
    to_fix = print_before - inserted
    if to_fix:
      # does order matter? I presume so...
      ordered_insert = [x for x in update if x in to_fix]
      for before in ordered_insert:
        insert(before)
    inserted.add(page)
    new_order.append(page)

  for page in update:
    insert(page)

  return new_order


def part1():
  tot = 0
  for update in updates:
    if correct_order(update):
      tot += mid(update)

def part2():
  tot = 0
  for update in updates:
    if not correct_order(update):
      tot += mid(fix(update))

print(part1())
print(part2())
