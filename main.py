# Basic calculator

a = " W E L C O M E "

print(a.center(85, "*"))
print()

num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))

print()

print("Addition = 1 \nSubtraction = 2 \nMultiplication = 3 \nDivision = 4 ")

operation = input("Enter operation number:")

if int(operation) > 4:
  print("invalid Operation")

elif int(operation) == 1:
  print("Ans:", int(num1) + int(num2))

elif int(operation) == 2:
  print("Ans:", int(num1) - int(num2))

elif int(operation) == 3:
  print("Ans:", int(num1) * int(num2))

elif int(operation) == 4:
  print("Ans:", int(num1) / int(num2))
