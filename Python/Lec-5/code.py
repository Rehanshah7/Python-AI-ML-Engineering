# 1. Write a Python program to read a file line by line and print the word found in the file.
print("Write a Python program to read a file line by line and print the word found in the file")
with open("sample.txt", "r") as file:
    for(line) in file:
        if "python" in line:
            print(f"Word 'python' is present in the file")
            break


# Create a program that opens names.txt file, write 5 names(one per line) enetered by user then open the same file in read mode and prints all names.
print("\n" + "Create a program that opens names.txt file, write 5 names(one per line) enetered by user then open the same file in read mode and prints all names")
with open("names.txt", "w") as file:
    for i in range(5):
        name = input("Enter name: ")
        file.write(name + "\n")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip is a built in function which deletes all the trailing spaces before and after


# Create a program that opens a file log.txt in append mode, add new log entry(Program run successfully), opens the file in read mode and prints all logs.
print("\n" + "Create a program that opens a file in append mode, add new log entry(Program run successfully), opens the file in read mode and prints all logs")
with open("log.txt", "a") as file:
    file.write("Program run successfully" + "\n")

with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())


# Create a program that has list of numbers [5, 10, 15, 20, 25], use a list comprehension to list a number which is greater than 15 and prints a new list.
print("\n" + "Create a program that has list of numbers [5, 10, 15, 20, 25], use a list comprehension to list a number which is greater than 15 and prints a new list")
list_of_int = [5, 10, 15, 20, 25]
new_list = [i for i in list_of_int if i > 15]
print(new_list)


# Create a Python dictionary of 3 cities and their populations. Save it to cities.json Then load the JSON and print each city and its population. Ask the user for a new city & its population - update this info in the json file.
print("\n" + "Create a Python dictionary of 3 cities and their populations. Save it to cities.json Then load the JSON and print each city and its population. Ask the user for a new city & its population - update this info in the json file.")
import json

with open("cities.json", "r") as file:
    data = json.load(file)
    for city, population in data.items():
        print(f"{city}: {population}")

with open("cities.json", "r") as file:
    data = json.load(file)
    city = input("Enter city: ")
    population = int(input("Enter population: "))
    data[city] = population

with open("cities.json", "w") as file:
    json.dump(data, file)

with open("cities.json", "r") as file:
    data = json.load(file)
    for city, population in data.items():
        print(f"{city}: {population}")


# Write a program that tries to open data.txt in read mode. If the file does not exist, catch the exception and print "File not found!"
print("\n" + "Write a program that tries to open data.txt in read mode. If the file does not exist, catch the exception and print 'File not found!'")
try:
    with open("data.txt", "r") as file:
        print(file.read())
        
except FileNotFoundError:
    print("File not found!")