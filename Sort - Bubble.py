def bubbleSort(a):
  for i in range(len(a)-1 , -1, -1):
    for j in range(i):
      if a[j]>a[j+1]:
        temp=a[j+1]
        a[j+1]=a[j]
        a[j]=temp
  return a

a=[9,5,8,1,6,3]
bubbleSort(a)