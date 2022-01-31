vowels = {"a", "e", "i", "o", "u"}
word = set(input("Provide a word to search for vowels: "))
found = vowels & word
print(found)