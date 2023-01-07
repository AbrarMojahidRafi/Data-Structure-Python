arr=[1,2,3,4,5,6,7]
searchElem=50

isFound=False
left=0
right=len(arr)-1
# for i in range(len(arr)//2):
while left <= right: # uporer line ar eta same jinish. ekta use korleii hbe
                        # basically this while loop is collected from internet
  mid = (left + right)//2
  if arr[mid] == searchElem:
    print(f"element founded at {mid} index")
    isFound=True
    break
  elif arr[mid] < searchElem:
    left=mid+1
  else:
    right=mid-1

if isFound == False:
  print("Element is not found")