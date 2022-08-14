import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']


def menu():
    while True:
        print("PASSWORD GENERATOR")
        print("1. Generate A New Password")
        print("2. Recall Generated Password")
        print("3. Exit")
        ch=int(input("Enter your choice: "))

        if ch==1:
            generate()
        elif ch==2:
            recall()
        elif ch==3:
            break
        else:
            print("Enter a valid choice!")
            print()

def generate():
    inputwords=input("Enter a list of keywords: ")
    words = list(inputwords.split(" "))
    length=int(input("Enter the length of the password: "))


    combined = lowercase + uppercase + numbers + words

    password = random.choice(lowercase) + random.choice(uppercase) + random.choice(numbers) + random.choice(symbols)

    for i in range(length-4):
        password = password + random.choice(combined)

    with open("keywords.txt","a") as f:
        f.write(inputwords + ":" + password + "\n")

    print("Your password is provided below!")
    print()
    print(password)
    print()

def recall():
    keyword_recall = input("Enter the keyword you have used: ")
    f=open("keywords.txt")
    for i in f.readlines():
        i=i.split(":")
        if keyword_recall == i[0]:
            print("Keyword Found! The password is given below.")
            print()
            print(i[1])

menu()