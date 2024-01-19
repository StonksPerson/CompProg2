import math as math

people = ""
peopleNames = []
idx = 0
isValid = False
while not isValid:
    people = input("How many people in your party? ")
    if people.isnumeric():
        people = int(people)
        break
    print("Invalid")

for i in range(people):
    peopleNames.append(input(f"What is your name ({i + 1})? "))

order = []
answer = []

entrees = [
    {"price": 5, "name": "steak"},
    {"price": 25, "name": "chicken"},
    {"price": 10, "name": "fish"},
    {"price": 70, "name": "lettuce"}
]
drinks = [
    {"price": 5, "name": "dr. pepper"},
    {"price": 2, "name": "sprite"},
    {"price": 7, "name": "coke"},
    {"price": 4, "name": "diet coke"}
]
dessert = [
    {"price": 20, "name": "ice cream"},
    {"price": 20, "name": "cake"},
    {"price": 22, "name": "cheese cake"},
    {"price": 23, "name": "sunday"}
]

def ask(items, name):
    isValid = False
    menu = ""

    for i in range(50):
        print()

    for i in items:
        menu += i["name"] + " $" + str(i["price"]) + ", "

    print(menu)

    while not isValid:
        answer = input(f"What do you want for your {name}, {peopleNames[idx]}? ")
        for i in items:
            if i["name"] == answer:
                isValid = True
                return i
                break
        print("Invalid")

def recipt(order):
    total = 0
    isValid = False
    while not isValid:
        tip = input("How much do you want to tip? ")
        if tip.isnumeric():
            tip = int(tip)
            isValid = True
        else: print("Invalid")

    for i in order:
        total += i['price']
        print(f"{i['name']} ${i['price']}")
    print(f"tax: ${math.floor(total * 0.061 * 100)/100}")
    print(f"tip: ${tip}")
    total = math.floor(total * 1.061 * 100) /100 + tip
    print("---------")
    print(f"total: ${total}")

for i in range(50):
    print()

for i in range(people):

    order.append(ask(entrees, "entree"))
    order.append(ask(drinks, "drink"))
    order.append(ask(dessert, "dessert"))
    idx += 1

for i in range(50):
    print()

recipt(order)