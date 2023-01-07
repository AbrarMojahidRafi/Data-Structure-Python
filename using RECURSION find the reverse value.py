def reversing(userValue):
  if userValue=="":
    return ""
  return reversing(userValue[1:])+userValue[0]
  
reversing("12345")