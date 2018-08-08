#!/usr/bin/env python
# -*- coding: utf-8 -*-

'my first module'

__author__ = 'John Zhang'

import sys

# 兼容引入外部模块
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

# 私有函数命名
def _privateFunc():
  print('1 args')

def test():
  args = sys.argv
  if len(args) == 1:
    _privateFunc()
  elif len(args) == 2:
    print('second args %s' % args[1])
  else:
    print('too many args')

if __name__ == '__main__':
  test()
