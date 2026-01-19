# Create a python program that manages a dictionary of words and their meanings. 
dictionary = {}
while(True):
    print(" 1.Add new word\n 2.Find meaning of word\n 3.Display dictionary\n 4.Delete a word\n 5.Modify the meaning of the word\n 6.Quit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        word=input("Which word would you like to add to the dictionary?")
        if word in dictionary:
            print(word,"already exists")
        else:
            meaning=input("What is the meaning of word? ")
            dictionary[word]=meaning

    elif choice==2:
        word=input("Which word meaning are you looking for? ")
        if word not in dictionary:
            print("No such word exists in the dictionary")
        else:
            print(dictionary[word])

    elif choice==3:
        for key,value in dictionary.items():
            print(key,value)

    elif choice==4:
        word=input("Which word you want to delete? ")
        if word in dictionary:
            del dictionary[word]
        else:
            print("no such word")

    elif choice==5:
        word=input("Which word's meaning you would like to change? ")
        if word not in dictionary:
            print("No such word in dictionary")
        else:
            meaning=input("What's the meaning? ")
            dictionary[word]=meaning

    elif choice==6:
        print("Thank you! visit again!")
        break
    else:
        print("Invaild choice")