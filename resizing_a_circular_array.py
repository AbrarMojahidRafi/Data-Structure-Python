"""
index: 0  1  2  3  4
circ=[20,30,40,50,10]
      index:   0  1  2 3  4  5  6
after resize: [40,50,0,0,10,20,30]
""" 


def resize(circ,start,size):
  a = circ
  newArray = [0]*(len(a)+2)
  indexVal = start
  newArrayIndex = start
  for i in range(len(a)):
    newArray[newArrayIndex] = a[indexVal]
    indexVal = (indexVal+1)%(len(a))
    newArrayIndex = (newArrayIndex+1)%(len(newArray))
  return newArray

circ=[20,30,40,50,10]   #creating a circular array with start 4 and size 5
circ=resize(circ,4,5) 
print(circ)
