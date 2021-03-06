
def merge(arr, l, m, r):   # 
  n1 = m - l + 1 
  n2 = r- m 
  L = [ arr[l+i] for i in range(n1) ] 
  R = [ arr[m+1+i] for i in range(n2) ] 

  i = 0 
  j = 0 
  k = l 
  while i < n1 and j < n2 :
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
    
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1


def mergeSort(arr,l,r):

  if l < r: 
    m = (l+(r-1))//2 
    mergeSort(arr, l, m) 
    mergeSort(arr, m+1, r) 
    merge(arr, l, m, r) 

arr = [19, 101, 33, 5, 6, 7,2,44,72,12,1,0] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
  print ("%d" %arr[i], end=" ")

mergeSort(arr,0,n-1) 
print("\n\nSorted array is") 
for i in range(n): 
  print ("%d" %arr[i], end = " ")

