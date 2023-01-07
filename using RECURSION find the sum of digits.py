# way one:
def sumOfDigits(givenString):
  if givenString=="":
    return 0
  return int(givenString[0]) + sumOfDigits(givenString[1:])

sumOfDigits("12345")


################################################


# way two:
# def sumOfDigit(givenDigit):
#   if givenDigit==0:
#     return 0
#   else:
#     lastDigit = givenDigit%10
#     return lastDigit + sumOfDigit(givenDigit//10)

# sumOfDigit(12345)