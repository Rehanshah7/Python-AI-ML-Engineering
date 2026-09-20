# Write a program that takes as input. Using conditional statements, calculate the final tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%
print("Write a program that takes as input. Using conditional statements, calculate the final tax rate based on these rules")
salary = float(input("Enter your salary: "))
if (salary < 30000):
    tax_rate = 0.05
    print("Your tax rate is 5% and you have to pay:", salary * tax_rate)
elif (salary >= 30000 and salary <= 70000):
    tax_rate = 0.15
    print("Your tax rate is 15% and you have to pay:", salary * tax_rate)
else:
    tax_rate = 0.25
    print("Your tax rate is 25% and you have to pay:", salary * tax_rate)


# Write a function that takes two integers and and prints all even numbers between them (inclusive).
print("\n" + "Write a function that takes two integers and and prints all even numbers between them (inclusive)")
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)


# Write a function that prints the digits of a number
print("\n" + "Write a function that prints the digits of a number")
number = int(input("Enter a number: "))
while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10


# Write a function that prints the count of digits of a number
print("\n" + "Write a function that prints the count of digits of a number")
number = int(input("Enter a number: "))
count = 0
while number > 0:
    digit = number % 10
    count += 1
    number = number // 10

print("Count of digits:", count)


# Write a function that prints the sum of digits of a number
print("\n" + "Write a function that prints the sum of digits of a number")
number = int(input("Enter a number: "))
sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number = number // 10

print("Sum of digits:", sum)


# Write a program to print the 1 to 100 which are divisible by 3 and 5
print("\n" + "Write a program to print the 1 to 100 which are divisible by 3 and 5")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”
print("\n" + "Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”")
while True:
    number = input("Enter a number (or type 'Quit' to exit): ")
    if number == "Quit":
        break
    number = int(number)
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


# Letʼs create a Simple calculator that performs arithmetic operations. Create a function that performs addition, subtraction, multiplication, or division based on the parameter
print("\n" + "Let's create a Simple calculator that performs arithmetic operations. Create a function that performs addition, subtraction, multiplication, or division based on the parameter")
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 // num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
result = calculator(num1, num2, operation)
print("Result:", result)


# Write a function that returns a True if is a prime number and otherwise False, using a loop
print("\n" + "Write a function that returns a True if is a prime number and otherwise False, using a loop")
def is_Prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = int(input("Enter a number: "))
if is_Prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


# Letʼs create a “Number Guessing Game”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
# • if the guess is above the number"Too high"
# • if the guess is below"Too low"
# • if the guess matches
print("\n" + "Let's create a 'Number Guessing Game'. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:")
def number_guessing_game(secret_number):
    while True:
        guess = int(input("Guess the secret number: "))
        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("Congratulations! You guessed the secret number.")
            break

secret_number = 42
number_guessing_game(secret_number)