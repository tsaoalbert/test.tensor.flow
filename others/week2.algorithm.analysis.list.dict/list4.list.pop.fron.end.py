
"""
There are a couple of things to notice about Listing 4. 
The first is the statement from __main__ import x. 
  Although we did not define a function we do want to be able to use the list 
  object x in our test. 
  This approach allows us to time just the single pop statement and get the most accurate measure of the time for that single operation. 
"""

import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
popzero.timeit(number=1000)
4.8213560581207275

x = list(range(2000000))
popend.timeit(number=1000)
0.0003161430358886719
