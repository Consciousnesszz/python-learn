#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'my first module'

__author__ = 'John Zhang'

import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('1 args')
  elif len(args) == 2:
    print('second args %s' % args[1])
  else:
    print('too many args')

if __name__ == '__main__':
  test()
