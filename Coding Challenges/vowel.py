
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