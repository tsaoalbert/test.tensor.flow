
import time, random

def mergeSort(alist, i=0 ):


  if len(alist)>1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    mergeSort(lefthalf, i+1)
    mergeSort(righthalf, i+1)

    i=0
    j=0
    k=0
    while i<len(lefthalf) and j<len(righthalf):
      if lefthalf[i]<righthalf[j]:
        alist[k]=lefthalf[i]
        i=i+1
      else:
        alist[k]=righthalf[j]
        j=j+1
      k=k+1

    while i<len(lefthalf):
      alist[k]=lefthalf[i]
      i=i+1
      k=k+1

    while j<len(righthalf):
      alist[k]=righthalf[j]
      j=j+1
      k=k+1



def selectionSort(alist):

  for i in range(len(alist)-1,0,-1):
    j=i
    for k in range(0,i):
      if alist[k]>alist[j]:
        j = k 
    alist[i], alist[j] = alist[j], alist[i]


L= list ( range(500) )
random.shuffle (L)
print ("Selection Sort:")
start = time.time()
selectionSort(L)      #xxx
end = time.time()
print ( end-start)

L= list ( range(500) )
random.shuffle (L)
print("Merge Sort")
start = time.time()   # xxx
mergeSort(L)
end = time.time()
print ( end-start)

