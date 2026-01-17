word = input("Enter your word: ")
char = input("Enter your character you want to search: ")
for letter in word:
    if letter == char:
        print("Character found in the word", letter)
        break
    else:
        print("Character not found! in the word",word)