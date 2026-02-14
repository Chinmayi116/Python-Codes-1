dictionary={}
while(True):
    print("1.Add new word\n 2.Find meaning of word\n 3.Display Disctionary\n 4.Delete word\n 5.Modify the meaning of word\n 6.Quit")
    choice=int(input("Enter your choice"))

    if choice==1:
        word=input("Add new wold to the dictionary")
        if word in dictionary:
            print("Alredy world is there in dictionary")
        else:
            meaning=input("Enter meaning of the word")
            dictionary[word]=meaning

    elif choice==2:
        meaning=input("which word meaning you want")
        if word not in dictionary:
            print("No such word")
        else:
            print(dictionary[word])
        
    elif choice==3:
        for key,value in dictionary.items():
            print(key,value)

    elif choice==4:
        word=input("Enter Word you want to delete")
        if word in dictionary:
            del dictionary[word]
        else:
            print("No such word")
    
    elif choice==5:
        word=input("Which word you want to modify")
        if word not in dictionary:
            print("No such word")
        else:
            meaning=input("Enter meaning of the word")
            dictionary[word]=meaning

    elif choice==6:
        print("Thank you")
        break
    else:
        print("Invaild Choice")