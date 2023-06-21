# Maximum of two numbers in Python
def max_number(num1, num2):
  if num1 > num2:
    print(f"Number1 {num1} is greater than number2 {num2}")
  else:
    print(f"Number2 {num2} is greater than number1 {num1}")

number1 = eval(input("Enter your number1: "))
number2 = eval(input("Enter your number2: "))
max_number(number1, number2)
