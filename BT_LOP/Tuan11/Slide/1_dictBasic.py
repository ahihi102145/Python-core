dictionary = {}

def add_word():
    word= input("Enter the word to add: ")
    meaning = input("Enter the meaning of the word: ")
    dictionary[word] = meaning
    print("Add successfuly :", dictionary)

def remove_word():
    word = input("Enter the word to remove: ")
    if word in dictionary:
        del dictionary[word]
        print("Remove successfuly :", dictionary)
    else:
        print("Word not in dictionary")

def update_word():
    word = input("Enter the word to update: ")
    if word in dictionary:
        meaning_new = input("Enter the meaning of the new word: ")
        dictionary[word] = meaning_new
        print("Update successfuly :", dictionary)
    else:
        print("Word not in dictionary")

def find_word():
    word = input("Enter the word to find: ")
    if word in dictionary:
        print("{}".format(dictionary[word]))
    else:
        print("Word not in dictionary")

def sort_word():
    print("Dictionary after sorting:")
    for word in sorted(dictionary.keys()):
        print(word)

def prin_dictionary():
    if  not dictionary:
        print("Dictionary is empty")
    for word , meaning in dictionary.items():
        print(f"{word} : {meaning}")
    print()

while True:
    print("\nDICTIONARY MANAGEMENT PROGRAM\n")
    print("1. add word")
    print("2. remove word")
    print("3. update word")
    print("4. find word")
    print("5. sort word")
    print("6. print dictionary")
    print("0. exit program")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_word()
    elif choice == 2:
        remove_word()
    elif choice == 3:
        update_word()
    elif choice == 4:
        find_word()
    elif choice == 5:
        sort_word()
    elif choice == 6:
        prin_dictionary()
    elif choice == 0:
        exit()
    else:
        print("Invalid choice")