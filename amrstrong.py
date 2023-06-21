# Python Program to check Armstrong Number
def armstrong(input):
  result = 0
  for i in input:
    result += pow(int(i), 3)
  if result == int(input):
    print("Armstrong numbers")
  else:
    print("Not")

armstrong("153")
