#!/usr/bin/env python
import collections

# Add to the right
d = collections.deque()
d.extend('abcdefg')

def genPerms(unused, perm_stack):
  n = len (unused );
  if n==0:
    print ( perm_stack)
  else:
    for k in range ( n ):
      perm_stack.append( unused[0] )
      unused.pop(0)
      genPerms(unused, perm_stack) 
      unused.append( perm_stack[ len(perm_stack) -1 ] )
      perm_stack.pop( len(perm_stack)-1 )

def main ():
  perm_stack = []
  unused = ["a","b","c"]  
  genPerms(unused, perm_stack)

if __name__ == "__main__":
    main()

