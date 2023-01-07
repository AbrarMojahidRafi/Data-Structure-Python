def findElem(givenArr, i, v):
  if i<len(givenArr):
    if givenArr[i]==v:
      return True
    else:
      return findElem(givenArr, i+1, v)
  else:
    return False


givenArr=[1,2,3,4,5,6,7,8]
findElem(givenArr, 0, 8)