# fi
if 5 == 5:
    print("Yes")

# User input
user_data = int(input("Enter a number: "))
if user_data != 5:
    print("Number is not 5")
    if user_data > 5:
        print("Number is bigger than 5")

# bollean
isHappy = False
if not isHappy:
    print("Sad")


# else
user_input = int(input("Enter a number: "))
if user_input == 5:
    print("Number is 5")
else:
    print("Number isn't 5")

#else if
user = int(input("Enter a number: "))
if user > 5:
    print("Number is bigger than 5")
elif user == 4:
    print("Number is 4")
else:
    print("Number is 5 or smaller")

# Несколько условий
a = int(input("Enter a number: "))
if a > 5 and a < 10:
    print(a, "> 5 and < 10")

# Тернарный оператор
# Full
data = input()
number = 5 if data == "Five" else 0
# if data == "Five":
#     number = 5
# else:
#     number = 0
print(number)
