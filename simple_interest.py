# Python Program for simple interest
def simple_interest(principal, time, rate):
  return (principal * time * rate) / 100

principal = eval(input("Enter your principal amount: "))
rate = eval(input("Enter your rate: "))
time = eval(input("Enter your units of time: "))
print(f"The total interest is {simple_interest(principal, time, rate)}")
