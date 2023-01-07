def binaryToDecimal_Recursion(binary, i, decimalNum):
  if len(binary)==i:
    return decimalNum
  else:
    if binary[i]=="0":
      decimalNum = decimalNum*2
    else:
      decimalNum = (decimalNum*2 + 1)
  return binaryToDecimal_Recursion(binary, i+1, decimalNum)

binaryToDecimal_Recursion("101",0,0)



###########################################################
# loop:

# def binaryToDecimal_Loop(binary):
#   dec = 0
#   for i in range(len(binary)):
#     if binary[i]=="0":
#       dec = dec*2
#     else:
#       dec = dec*2 + 1
#   return dec

# binaryToDecimal_Loop("101")