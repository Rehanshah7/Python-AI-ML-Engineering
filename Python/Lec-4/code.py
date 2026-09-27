from abc import ABC, abstractmethod

# create an online product store(name, price)
print("create an online product store(name, price)")
class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def info(self):
        return f"Product Name: {self.name}, Price: {self.price:.2f}"

    @classmethod
    def getCount(cls):
        return cls.count

    @staticmethod
    def calc_discount(price, discount):
        return price - (price * discount / 100)

p1 = Product("Laptop", 80_000)
print(p1.info())

p2 = Product("Mobile", 50_000)
print(p2.info())

print(f"Total products: {Product.getCount()}")

print(f"Discounted price of laptop: {Product.calc_discount(p1.price, 10):.2f}")
print(f"Discounted price of mobile: {Product.calc_discount(p2.price, 5):.2f}")


# Create a BankAccount class with attributes account_number, account_holder, balance and methods deposit, withdraw, get_balance
print("\n" + "Create a BankAccount class with attributes account_number, account_holder, balance and methods deposit, withdraw, get_balance")
class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount:.2f}, New Balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount:.2f}, New Balance: {self.balance:.2f}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

account = BankAccount("123456789", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: {account.get_balance():.2f}")


# Create a class Book with following attributes: title, author, list of reviews and add methods: add_review, get_reviews, count all reviews
print("\n" + "Create a class Book with following attributes: title, author, list of reviews and add methods: add_review, get_reviews, count all reviews")
class Book:
    __count = {}
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__reviews = []

        Book.__count[self.__title] = 0

    def add_review(self, review):
        self.__reviews.append(review)
        Book.__count[self.__title] += 1
        print(f"Review added: {review}")

    def get_reviews(self):
        return self.__reviews

    def count_reviews(self):
        return Book.__count[self.__title]

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book1.add_review("A masterpiece of literature.")
book1.add_review("An unforgettable experience.")
print("Reviews:", book1.get_reviews())
print("Total reviews:", book1.count_reviews())

book2 = Book("To Kill a Mockingbird", "Harper Lee")
book2.add_review("A classic novel.")
print("Reviews:", book2.get_reviews())
print("Total reviews:", book2.count_reviews())


# Create a class Student with private attributes __name, __roll_no, __marks. Provide getter and setter methods with validation (e.g. marks should be between 0 and 100, roll number should be positive between 0 to 100 and name should not be empty).
print("\n" + "Create a class Student with private attributes __name, __roll_no, __marks. Provide getter and setter methods with validation (e.g. marks should be between 0 and 100, roll number should be positive between 0 to 100 and name should not be empty).")
class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name:
            self.__name = name
        else:
            print("Name cannot be empty.")

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        if 0 < roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")

student = Student("John Doe", 25, 85)
print(f"Student Name: {student.get_name()}, Roll No: {student.get_roll_no()}, Marks: {student.get_marks()}")
student.set_name("Jane Doe")
student.set_roll_no(30)
student.set_marks(90)
print(f"Updated Student Name: {student.get_name()}, Roll No: {student.get_roll_no()}, Marks: {student.get_marks()}")


# Create a class Shape with methods area(). Create a subclass Circle, Rectangle and Triangle that override the area method to calculate the area of the respective shapes.
print("\n" + "Create a class Shape with methods area(). Create a subclass Circle, Rectangle and Triangle that override the area method to calculate the area of the respective shapes.")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print(f"Area of Circle: {circle.area():.2f}")
print(f"Area of Rectangle: {rectangle.area():.2f}")
print(f"Area of Triangle: {triangle.area():.2f}")


# Create a base class Vehicle with attributes like brand and model. Create a two sub classes Car and Bike that adds extra variables like number_of_seats for car and engine_cc for bike.
print("\n" + "Create a base class Vehicle with attributes like brand and model. Create a two sub classes Car and Bike that adds extra variables like number_of_seats for car and engine_cc for bike.")
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, number_of_seats):
        super().__init__(brand, model)
        self.number_of_seats = number_of_seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car = Car("Toyota", "Camry", 5)
bike = Bike("Honda", "CBR", 150)

print(f"Brand: {car.brand}, Model: {car.model}, Number of Seats: {car.number_of_seats}")
print(f"Brand: {bike.brand}, Model: {bike.model}, Engine CC: {bike.engine_cc}")


# Create an Abstract class Employee with an abstract method calculate_salary(). Create three subclasses Intern, FullTimeEmployee and ContractEmployee that implement the calculate_salary() method based on their respective salary structures.
print("\n" + "Create an Abstract class Employee with an abstract method calculate_salary(). Create three subclasses Intern, FullTimeEmployee and ContractEmployee that implement the calculate_salary() method based on their respective salary structures.")
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

intern = Intern(1000)
full_time_employee = FullTimeEmployee(50000, 5000)
contract_employee = ContractEmployee(200, 160)

print(f"Intern Salary: {intern.calculate_salary()}")
print(f"Full Time Employee Salary: {full_time_employee.calculate_salary()}")
print(f"Contract Employee Salary: {contract_employee.calculate_salary()}")


# Create a class Person that allows constructor to work with default parameters name only, name and age, name, age and address. Create a method display() to display the values of the attributes. As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.
print("\n" + "Create a class Person that allows constructor to work with default parameters name only, name and age, name, age and address. Create a method display() to display the values of the attributes. As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.")
class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        info = f"Name: {self.name}"
        if self.age is not None:
            info += f", Age: {self.age}"
        if self.address is not None:
            info += f", Address: {self.address}"
        print(info)

person1 = Person("Alice")
person2 = Person("Bob", 30)
person3 = Person("Charlie", 40, "123 Main St")

person1.display()
person2.display()
person3.display()


# Create a class Player with a class variable player_count, instance variable name and level. Track how many players were created.
print("\n" + "Create a class Player with a class variable player_count, instance variable name and level. Track how many players were created.")
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

player1 = Player("Alice", 1)
player2 = Player("Bob", 2)
player3 = Player("Charlie", 3)

print(f"Total number of players: {Player.player_count}")


# Create a following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.
print("\n" + "Create a following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.")
class Herbivore:
    def eat_plants(self):
        return "Eating plants"

class Carnivore:
    def eat_meat(self):
        return "Eating meat"

class Omnivore:
    def eat_both(self):
        return "Eating both"

class Bear(Herbivore, Carnivore, Omnivore):
    def roar(self):
        return "Roaring"

bear = Bear()
print(bear.eat_plants())
print(bear.eat_meat())
print(bear.eat_both())
print(bear.roar())