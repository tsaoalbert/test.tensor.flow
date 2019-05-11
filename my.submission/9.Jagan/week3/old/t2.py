

# used to pick a better pivot value to enable the balanced partition
def pivot (alist, first, last):  # xxx explain this function
  if last > first+1:
    L=alist[first:last+1]       
    n = len(L)
    x = sorted(L)[ (n-1)//2 ]
    i = first + L.index(x)
    alist[first], alist[i] = alist[i], alist[first]
    
def quickSort(alist,d,e ):
  return quickSortHelper(alist,0,len(alist)-1, 0,d,e )
  

def quickSortHelper(alist,first,last, i, d, e):
  for j in range (first, last+1):
    d[i][j] =  alist[j]
  depth = i+1
  if first<last:
    splitpoint = partition(alist,first,last )
    d[i] = alist.copy()
    for j in range (i+1,len(e)):
        e[j][splitpoint] = "*" 
    x=quickSortHelper(alist,first,splitpoint-1, i+1,d,e )
    y=quickSortHelper(alist,splitpoint+1,last, i+1,d,e )
    depth = max (x,y)
  return depth
   
def partition(alist,first,last):
    
  pivot (alist, first, last)

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
      alist[leftmark], alist[rightmark]  = alist[rightmark], alist[leftmark]
  alist[first], alist[rightmark]  = alist[rightmark], alist[first]
  return rightmark
def preTrace (M):
    print ("Quick Sort: ")
    d=[]; e=[]
    n = len(M)
    for i in range ( n):
        d.append(M.copy()); 
        e.append([" "]*n)
    return d, e

def testQuickSort(L):
    n = len(L)
    d,e = preTrace ( sorted(L) );
    m = quickSort(L, d,e )
    X = list( range(m) ) + [ n-1]
    for i in range ( m):
        s = "{0:2}: ".format(i)
        print (s, end="")
        for j in range(n):
            x = d[i][j]; y = e[i][j]
            s = "{0:>2}{1:<2}".format(x,y)
            if (i!= m-1 and i>0 and e[i-1][j]=="*"):
              s = " "* len(s)  
            print ( s, end=" ")
        print ()

L = [54,26,93,17,77,31,44,55,20]
testQuickSort(L)
testQuickSort ([0,1,2,3])
testQuickSort ([4,3,2,1,0])

a=[7, 2,9, 3,4,10, 5,1, 6,8]  #Q4
b=[10,9,8,7,6,5,4,3,2,1]      #Q5
c=[1,2,3,4,5,6,7,8,9,10]      #Q6
d=['P','Y','T','H','O','N']   #Q7
for s in [a,b,c,d]:
    testQuickSort(s)

