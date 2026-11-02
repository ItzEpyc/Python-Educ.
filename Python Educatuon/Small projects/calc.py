num1 = int(input("Enter first number: "))
print("+, -, *, /")
math = (input("Enter a math sym: "))
num2 = int(input("Enter second number: "))

if math == "+":
    print(num1 + num2)
elif math == "-":
    print(num1 - num2)
elif math == "*":
    print(num1 * num2)
elif math == "/":
    print(num1 / num2)
else:
    print("Invalid input")
