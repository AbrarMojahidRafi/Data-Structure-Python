def insertingAnElementAtAnyIndexInTheMiddle(circArray, insertingIndex, insertingVal, startingIndex):
  # atfast we count the size of this array
  arr = circArray 
  size=0
  for i in arr:
    if i!=0:
      size+=1

  if size < len(arr):
    newArray = [0]*len(arr)
    startIndex = startingIndex
    for i in range(len(arr)):
      if startIndex < insertingIndex : 
        newArray[startIndex] = arr[startIndex]
        startIndex=(startIndex+1)%len(arr)
        #print(newArray)
      else:
        j=len(arr)-1
        while (j>insertingIndex-1):
          newArray[(j+1)%len(arr)]=arr[j]
          #print(newArray)
          j=j-1
        newArray[insertingIndex]=insertingVal
    return newArray
  else:
    pass # ekhane new array create kore last element er por val insert krbo



circArray=[0,0,1,2,3,4,5]
startingIndex=2
insertingIndex = 4 #int(input("Enter insertingIndex No: "))
insertingVal = 28 #int(input("Enter insertingVal: "))
print(insertingAnElementAtAnyIndexInTheMiddle(circArray, insertingIndex, insertingVal, startingIndex))
