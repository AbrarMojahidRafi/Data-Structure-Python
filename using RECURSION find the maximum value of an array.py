def recMax(givenArr,i,v):
  if i==len(givenArr):
    return v
  elif givenArr[i] > v:
    return recMax(givenArr, i+1, givenArr[i])

givenArr=[1,2,3,4,5]
print(recMax(givenArr,0,0))