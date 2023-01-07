givenArray=[1,2,3,4,5]
k=4

#-------------------------------------------
tempArray=[0]*k
i=len(givenArray)-k
tempIndex=0 
while(i<=len(givenArray)-1):
  tempArray[tempIndex]=givenArray[i]
  tempIndex=tempIndex+1
  i=i+1  
#print(tempArray)
#-------------------------------------------


#---------------------------------------------
rsi=len(givenArray)-1                       #|
while(rsi>=k):                              #|--------> output:  [1, 2, 1, 2, 3]
  givenArray[rsi]=givenArray[rsi-k]         #|
  rsi=rsi-1                                 #|
#print(tempArray)
#---------------------------------------------

indexVal=0
while ( indexVal<len(tempArray) ):
  givenArray[indexVal] = tempArray[indexVal]
  indexVal+=1
   
  

print(givenArray)