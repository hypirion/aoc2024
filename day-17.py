#!/usr/bin/env pypy3

import sys, re
from collections import namedtuple

regs, prog = sys.stdin.read().strip().split('\n\n')

regs = list(map(int, re.findall('\d+', regs)))
prog = list(map(int, re.findall('\d+', prog)))

A = 0
B = 1
C = 2

class Program:
  def __init__(self, r, p):
    self.ip = 0
    self.r = r[:]
    self.p = p[:]
    self.out = []

  def copy(p):
    return Program(p.r[:], p.p, p.out[:])

  def lit(p):
    return p.p[p.ip+1]

  def combo(p):
    r = p.r
    return {0:0, 1:1, 2:2, 3:3, 4:r[A], 5:r[B], 6:r[C]}[p.lit()]

  def halted(p):
    return len(p.p) <= p.ip

  def step(p):
    r = p.r
    op = p.p[p.ip]
    lit = p.lit()
    combo = p.combo()
    if op == 0:
      r[A] = r[A]//(1 << combo)
    if op == 1:
      r[B] = r[B] ^ lit
    if op == 2:
      r[B] = combo & 0b111
    if op == 3:
      if r[A] != 0:
        p.ip = lit - 2
    if op == 4:
      r[B] = r[B] ^ r[C]
    if op == 5:
      p.out.append(combo & 0b111)
    if op == 6:
      r[B] = r[A]//(1 << combo)
    if op == 7:
      r[C] = r[A]//(1 << combo)
    p.ip += 2

  def run(p):
    while not p.halted():
      p.step()
    return p.out

def combo_arg_str(arg):
  if arg <= 3:
    return arg
  if arg <= 6:
    return 'ABC'[arg-4]
  return '?'

def prog_to_funcalls(prog):
  ops = ['adv', 'bxl', 'bst', 'jnz', 'bxc', 'out', 'bdv', 'cdv']
  res = []
  for i in range(len(prog)//2):
    op = prog[2*i]
    arg = prog[2*i + 1]
    if op == 0:
      den_mul = combo_arg_str(arg)
      if isinstance(den_mul, int):
        print('A = A // {}'.format(1 << den_mul))
      else:
        print('A = A // (1 << {})'.format(den_mul))
    elif op == 1:
      print('B = B ^', arg)
    elif op == 2:
      combo = combo_arg_str(arg)
      if isinstance(combo, int):
        print('B =', combo & 0b111)
      else:
        print('B = {} & 0b111'.format(combo))
    elif op == 3:
      print('goto', combo_arg_str(arg))
    elif op == 4:
      print('B = B ^ C')
    elif op == 5:
      print('print({} & 0b111)'.format(combo_arg_str(arg)))
    elif op == 6:
      den_mul = combo_arg_str(arg)
      if isinstance(den_mul, int):
        print('C = A // {}'.format(1 << den_mul))
      else:
        print('C = A // (1 << {})'.format(den_mul))
    elif op == 7:
      den_mul = combo_arg_str(arg)
      if isinstance(den_mul, int):
        print('C = A // {}'.format(1 << den_mul))
      else:
        print('C = A // (1 << {})'.format(den_mul))


def part1():
  res = Program(regs, prog).run()
  return ','.join(map(str, res))


def search(a, i):
  # work on 3 and 3 bits (the program peeks at the 4/5th bit, hence this
  # search)
  if len(prog) == i:
    return a
  p = prog[-i-1:]
  for j in range(0b1000):
    r = regs[:]
    r[A] = (a << 3) | j
    res = Program(r, prog).run()
    if res == p:
      rec = search(r[A], i+1)
      if rec:
        return rec
  return None

def part2():
  return search(0, 0)


print(part1())
print(part2())

#exit(1) # remove to run on data.in
