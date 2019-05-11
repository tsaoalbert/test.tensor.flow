"""
#1 Devise an experiment to verify that the list index operator is O(1)
#2 Devise an experiment to verify that get item and set item are O(1) for dictionaries.
"""

import timeit
import random as r

list_index = timeit.Timer("for i in L: x[i]", "from __main__ import x,L")

dict_get = timeit.Timer("for i in L: y[i]", "from __main__ import y,L")
dict_set = timeit.Timer("for i in L: y[i]=-i", "from __main__ import y,L")

inc = 1000000
n = inc
print("%8s: %15s %15s %15s" %("size", "list_index", "dict_get", "dict_set" ))
num_repeats = 100000
for j in range(10):
    x = list(range(n))  # a list of n items 
    y = []
    for k in x:
      y += (k,k)
    L = [ r.randint(0,n-1) for _ in range( 100 )]

    time_list_index = list_index.timeit(number=num_repeats)
    time_dict_get =   dict_get.timeit(number=num_repeats)
    time_dict_set =   dict_set.timeit(number=num_repeats)

    print("%8d: %15.5f %15.5f %15.5f " %(n, time_list_index, time_dict_get, 
          time_dict_set, ))
    n += inc
