# 28/2/2024

# accept two number and display the greatest number
num1 = int(input("enter a number="))
num2 = int(input("enter a 2 number="))

if num1 < num2:
    print(f"{num2} is greather than {num1}")
elif num1 > num2:
    print(f"{num1} is greather than {num2}")
else:
    print(f"number {num1} and {num2} is equal")