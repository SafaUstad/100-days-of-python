try:
  age = int(input("Enter your age:"))
except ValueError:
  print("You must enter a numeric value. e.g.,15")
  age = int(input("Enter your age:"))
