"""
#3 Devise an experiment that compares the performance of the 
      del operator on lists and dictionaries.
"""

import timeit
import random as r

list_del = timeit.Timer("for i in L: lis.remove(i)", "from __main__ import lis,L")
dict_del = timeit.Timer("for i in L: dict.pop(i,None)", "from __main__ import dict,L")

inc = 100000
n = inc
print("%8s: %15s %15s " %("index", "list_del", "dict_del" ))
num_repeats = 100000
num_repeats = 1
m = 100
for j in range(10):
    lis = list(range(n))
    dict = {}
    for k in lis:
      dict[k] = k
    L = []
    for i in range (m):
      L.append(n*i/m)

    time_list_del = list_del.timeit(number=num_repeats)
    time_dict_del = dict_del.timeit(number=num_repeats)

    print("%8d: %15.5f %15.5f " %(n, time_list_del, time_dict_del  ))
    n += inc
