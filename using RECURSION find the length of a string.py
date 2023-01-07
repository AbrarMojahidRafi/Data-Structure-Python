def findLen(s):
  if s=="":
    return 0
  else:
    return 1+findLen(s[1:])

findLen("abrar123")