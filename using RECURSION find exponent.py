def exponent(value, power):
  if power is 0:
    return 1
  return value*exponent(value, power-1)

exponent(4, 3)