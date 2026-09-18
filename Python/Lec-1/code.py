# Lec-1 Assignment

# 1. Average of 2 numbers
num1_a = 10
num2_a = 30
average_a = int((num1_a + num2_a) / 2)
print(average_a, "\n")

# 2. Write a program that asks the user for their name and age, then prints
name_b = input("Enter your name: ")
age_b = int(input("Enter your age: "))
print("Hello, " + name_b + "! You are " + str(age_b) + " years old.", "\n")

# 3. Take two numbers as input from the user and print their sum, difference, product, and quotient
num1_c = int(input("Enter first number: "))
num2_c = int(input("Enter second number: "))
print("Sum of 2 numbers:", num1_c + num2_c)
print("Difference of 2 numbers:", num1_c - num2_c)
print("Product of 2 numbers:", num1_c * num2_c)
print("Quotient of 2 numbers:", num1_c / num2_c, "\n")

# 4. Ask the user to enter two integers and one float. Convert them all to floats and print their average
num1_d = int(input("Enter first number: "))
num2_d = float(input("Enter second number: "))

print("Average of 2 numbers:", (float(num1_d) + float(num2_d)) / 2, "\n")

# 5. The user enters a string containing a number (e.g., ). Convert it to an integer, float and then string again and then print all the values
string_e = input("Enter a string containing a number: ")
print("Integer:", int(string_e))
print("Float:", float(string_e))
print("String:", str(string_e), "\n")

# 6. Evaluate and print the result of the following expression: x = 10 + 3 * 2 ** 2
x_f = 10 + 3 * 2 ** 2
print(x_f, "\n")

# 7. Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit
celsius = input("Enter temperature in Celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit, "\n")

# 8. Take the radius (r) as user input and print the area of a circle
r = int(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle:", area, "\n")

# 9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and compute simple interest
p_si = int(input("Enter principal: "))
r_si = int(input("Enter rate: "))
t_si = int(input("Enter time: "))
si = (p_si * r_si * t_si) / 100
print("Simple interest:", si, "\n")

# 10. Swap two numbers entered by the user using a temporary variable
num1_g = int(input("Enter first number: "))
num2_g = int(input("Enter second number: "))
temp = num1_g
num1_g = num2_g
num2_g = temp
print("Swapped numbers:", num1_g, num2_g, "\n")

# 11. Swap two numbers without using a temporary variable
num1_h = int(input("Enter first number: "))
num2_h = int(input("Enter second number: "))
num1_h = num1_h + num2_h
num2_h = num1_h - num2_h
num1_h = num1_h - num2_h
print("Swapped numbers:", num1_h, num2_h, "\n")

# 12. Take a decimal number as input (like ) and output its: integer and fractional parts
decimal = float(input("Enter a decimal number: "))
integer = int(decimal)
fractional = decimal - integer
print("Integer part:", integer)
print("Fractional part:", fractional, "\n")