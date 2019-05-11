import timeit
def quickSort(alist, k):
   quickSortHelper(alist,0,len(alist)-1,k)
   return alist[k]

def quickSortHelper(alist,first,last,k):
   if first<last: 
      splitpoint = partition(alist,first,last)
      if ( k == splitpoint ):
        return 
      elif (k< alist[splitpoint] ):
        quickSortHelper(alist,first,splitpoint-1,k)
      else: 
        quickSortHelper(alist,splitpoint+1,last,k)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def foo(alist,k=0):
  quickSort(alist,k);


from random import shuffle

for i in range (10):
  n = 100000*(i+1)
  k=n//2
  alist = list ( range(n) )
  shuffle( alist )
  x = timeit.Timer("quickSort(alist,k); ", "from __main__ import quickSort, alist,k")
  tx = x.timeit(5)
  print("%7d:  %15.6f" % (n, tx) )

