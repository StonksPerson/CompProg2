import math as math

print("hi")

print(f"{2+2}")

name = input("what is your name? ")

print(f"hello {name}")

word = input("type string: ")

def reverse(word):
    print_word = ""
    for i in range(len(word)):
        print_word += word[len(word) - i - 1]
    return print_word

print(reverse(word))

def check_even():
    number = int(input("input number"))
    if math.floor(number / 2) == number / 2:
        print("your number is even")
    else:
        print("it is not even")

def check_pallindrome(pallindrome):
    if pallindrome == reverse(pallindrome):
        print("it is a pallindrome")
    else: print("it is not a pallindrome")

check_pallindrome(input("type a word "))

def vowels(tmp_word):
    word = tmp_word.lower()
    vowels = 0
    for i in word:
        if i == "a":
            vowels += 1
        if i == "e":
            vowels += 1
        if i == "i":
            vowels += 1
        if i == "o":
            vowels += 1
        if i == "u":
            vowels += 1
        if i == "y":
            vowels += 0.5
    return vowels
print(vowels(input("type word: ")))

def capitalize_sentence():
    sentence = input("input a sentence ")
    print(sentence.title())

        

capitalize_sentence()

def find_biggest(array):
    biggest = 0
    for i in array:
        if i > biggest:
            biggest = i
    return i

print(find_biggest([1,10,20,40,10,5,20]))

def calc_sum(array):
    total = 0
    for i in array:
        total += i
    return total

print(calc_sum([1,10,20,40,10,5,20]))