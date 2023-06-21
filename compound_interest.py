# Python Program for compound interest
def compund_interest(principal, rate, time):
  amount = principal * pow((1 + rate/100), time)
  ci = amount - principal
  return ci

principal = eval(input("Enter your principal amount: "))
rate = eval(input("Enter your rate: "))
time = eval(input("Enter your units of time: "))
print(f"The compund interest is {compund_interest(principal, rate, time)}")
