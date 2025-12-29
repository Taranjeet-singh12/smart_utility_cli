print("Smart Utility CLI")
print("1. Age checker")
print("2. Odd/Even checker")
print("3. Bill Discount")
print("4. simple calculator")

choice = input("Choose an option (1-4)")

if choice =="1":
    age = int(input("Enter oyur age: "))

    if age < 0 or age > 150:
        print("Invalid age")
    elif age < 18:
        print("Minor")
    elif age < 60:
        print("Adult")
    else:
        print("Senior")

elif choice =="2":
    num = int(input("Enter a number: ."))

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

elif choice =="3":
    amount = float(input("Enter bill amount: "))

    if amount < 0:
        print("Invalid amount")
    elif amount < 500:
        print("No Discount")
    elif amount < 1000:
        print("10% Discount")
    else:
        print("20% Discount")

elif choice =="4":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0:
            print("cannot divided by zero")
        else:
            print(a / b)
    else:
        print("Invalid operation")

else:
    print("Invalid choice")
    