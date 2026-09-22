# Ask the user for a string and check whether it is a palindrome or not, A palindrome is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.
print("Enter a string to check whether it is a palindrome or not")
string = input("Enter a string: ")

reverse_string = ""

for ch in string:
    reverse_string = ch + reverse_string

if string == reverse_string:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")


print("\n" + "Enter a string to check whether it is a palindrome or not with built in method")
string = input("Enter a string: ")

if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")


# Given a list of integers compute the average of all numbers in the list
print("\n" + "Given a list of integers compute the average of all numbers in the list")
list_of_int = [1, 2, 3, 4, 5]
sum = 0
average = 0

for i in list_of_int:
    sum = sum + i

average = sum / len(list_of_int)
print("Average of all numbers in the list:", average)


Input two lists of integers from the user. Merge them into one list and sort the result
print("\n" + "Input two lists of integers from the user. Merge them into one list and sort the result")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
merged_list.sort()
print("Merged list:", merged_list)


# Given a tuple of integers, create:
# 1. A list of all even numbers
# 2. A list of all odd numbers
print("\n" + "Given a tuple of integers, create: A list of all even numbers, A list of all odd numbers")
tuple_of_int = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_list = []
odd_list = []

for i in tuple_of_int:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)


# Create a dictionary with keys = student name and values as marks Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
# depending on the operation they want to perform on the dictionary: 
# A - Add a new student and marks
# B - Update marks of an existing student
# C - Delete a student
# D - Display all students and marks
# E - Exit
print("\n" + "Create a dictionary with keys = student name and values as marks Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)"))

dictionary_student_name_marks = {}

while True:
    print("A - Add a new student and marks")
    print("B - Update marks of an existing student")
    print("C - Delete a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice from the above characters: ")

    match choice:
        case "A":
            student_name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            dictionary_student_name_marks[student_name] = marks
        case "B":
            student_name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            dictionary_student_name_marks.update({
                student_name: marks
            })
        case "C":
            student_name = input("Enter student name: ")
            del dictionary_student_name_marks[student_name]
        case "D":
            print(dictionary_student_name_marks)
        case "E":
            break
        case _:
            print("Invalid choice")


# Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]. Create a dictionary that maps each word to its length.
print("\n" + "Given a list of words: words = [apple, banana, kiwi, cherry, mango]. Create a dictionary that maps each word to its length.")
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dictionary_word_length = {}

for word in words:
    dictionary_word_length[word] = len(word)

print(dictionary_word_length)


Write a program that takes a string from the user and prints the number of spaces in the string.
print("\n" + "Write a program that takes a string from the user and prints the number of spaces in the string.")

string = input("Enter a string: ")
spaces = 0

for i in string:
    if i == " ":
        spaces += 1

print("Number of spaces in the string:", spaces)


# Write a program to check whether two lists share no common elements.
print("\n" + "Write a program to check whether two lists share no common elements.")

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

set1 = set(list1)
set2 = set(list2)

if set1.intersection(set2):
    print("Lists share common elements.")
else:
    print("Lists do not share common elements.")


# Given a list, print all elements that appear more than once in the list.
print("\n" + "Given a list, print all elements that appear more than once in the list.")

list1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]

set1 = set(list1)

for i in set1:
    if list1.count(i) > 1:
        print(i, "appears more than once in the list.")