"""

2.4 Given a list of numbers in random order, write an algorithm that works
      in O(nlog(n)) to find the kth smallest number in the list.
2.5 Improve the algorithm from the previous problem to be linear? 
"""

#import timeit
from timeit import Timer
import random as r

def  selection (L,k):
  return sorted(L)[k]


list_sel = Timer("selection(lis, k) ", "from __main__ import selection, lis,k")
fast_sel = Timer("selection(lis, k) ", "from __main__ import selection, lis,k")

inc = 100000
n = inc
print("%8s: %15s %15s " %("index", "list_sel", "fast_sel" ))
num_repeats = 100000
num_repeats = 1000
for j in range(10):
    lis = list(range(n))
    k = r.randint (0,n-1)
    time_list_sel = list_sel.timeit(number=num_repeats)
    time_fast_sel = fast_sel.timeit(number=num_repeats)

    print("%8d: %15.5f %15.5f " %(n, time_list_sel, time_fast_sel  ))
    n += inc
