#!/usr/bin/env python
import collections


def genPerms(queue, perm_stack):
  n = len (queue );
  if n==0:
    #print ( perm_stack)
    print ()
  else:
    for k in range ( n ):
      print ( queue)
      perm_stack.append( queue.popleft() ) 
      genPerms(queue, perm_stack) 
      queue.append( perm_stack.pop( ) )
      print ( queue)

def main ():
  perm_stack = collections.deque()
  queue = collections.deque()
  queue.extend('abc')
  genPerms(queue, perm_stack)

if __name__ == "__main__":
    main()

