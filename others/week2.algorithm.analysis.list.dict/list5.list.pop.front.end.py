"""
#listing 5
While our first test does show that pop(0) is indeed slower than pop(), 
it does not validate the claim that pop(0) is O(n) while pop() is O(1). 

To validate that claim we need to look at the performance of both calls 
over a range of list sizes. 

Listing 5 implements this test.
"""

from timeit import Timer

popFront = Timer("x.pop(0)", "from __main__ import x")
popRear = Timer("x.pop()", "from __main__ import x")
print("%15s, %15s" % ("pop(0)", "pop()") )

for i in range(1000000,100000001,1000000):
    x = list(range(i))
    timePopFront = popFront.timeit(number=1000)
    x = list(range(i))

    timePopRear = popRear.timeit(number=1000)
    print("%15.5f, %15.5f" %(timePopFront,timePopRear))

