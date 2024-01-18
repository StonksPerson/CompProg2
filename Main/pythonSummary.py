# # variables

# text = ""
# number = 10
# true_false = True

# # lists

# my_bb_list = [text, number, true_false, 45, "Hi"]
# two_list = [1,2,3,4]


# # dictionaries

# dictionary = { "age": 500, "name": "dave" }

# print(dictionary["age"])

# # conditionals

# if true_false:
#     print('wawa')
# elif 10 > 5:
#     print("asdf")
# else:
#     print("Bambawaba")

# #loops

# numbers = [1,2,3,4,5]

# for key in dictionary:
#     print(student[key])

# # functions 

# def greet(name, age):
#     print(f"hello {name} you are {age}!!!11!11")

# students = [
#     {"name": "kyle","age": 50},
#     {"name": "mike","age": 87},
#     {"name": "dave","age": 1}
# ]

# for i in students:
#     greet(s)

# class car:
#     # CONSTRUCTOR
#     def __init__(self, color, seats, make, model):
#         self.color = color
#         self.mileage = 0
#         self.seats = seats
#         self.make = 0
#         self.model = model

# honda_accord = Car('blue', 5, "honda", "accord")
# pt_crusier = Ccar('red', 5, 'chrysler', "pt cruiser")

# print(pt_crusier)

class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def check_balance(self):
        print(f"{self.name} balance: ${self.balance}")

    def change_name(self, new_name):
        self.name = new_name

    def withdraw(self, amt):
        if amt > self.balance:
            print("Sorry, insufficient funds")
            return
        else:
            self.balance -= amt

    def deposit(self, amt):
        self.balance += amt

accounts = []

choice = input("""
    what would you like to do?

    1. create account
    2. check balance
""")

if choice == "1":
    name = input("what would you like to name the account? ")
    accounts.append(Account(name))

for a in accounts:
    print(a.name)