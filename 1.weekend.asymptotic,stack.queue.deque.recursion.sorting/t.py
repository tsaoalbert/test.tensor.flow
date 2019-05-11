
#Give the Big-O performance of the following code fragment:
def findRepeated(L):
  """
    determines whether all elements in a given list L are distinct
  """
  n=len(L)
  for i in range(n):
    for j in range(i+1, n):
      if L[i]==L[j]:
        return True
  return False
