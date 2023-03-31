import csv
def GetData():
    l = csv.reader(open("Passwords.csv","r"))
    L = []
    for row in l:
        L.append(row)
    return L

def NewUserID(tempList):
    while True:
        inlist = False
        userID = input("Enter User ID: ")
        for row in tempList:
            if userID == row[0]:
                print("Select another user ID!")
                inlist = True
                break
        if inlist == False:
            break
    return userID
        
def NewPassword():
    while True:
        password=input("Enter a password which includes at least 8 chars,uppercase,lowercase, numbers and a special char:\n")
        score = 0
        if len(password)>= 8:
            score+=1
            for char in password:
                if char.isupper():
                    score+=1
                    break
            for char in password:
                if char.islower():
                    score+=1
                    break
            for char in password:
                if char.isdigit():
                    score+=1
                    break
            for char in password:
                if char in "!£$%&<@":
                    score+=1
                    break
        if score <=2:
            print("Too weak password!")
        elif score ==3 or score ==4:
            print("This password could be improved")
            tryAgain = input("Do you want to try again? (Y)/(N): ").strip().lower()
            if tryAgain == "n":
                break
        else:
            print("You've selected a strong password!")
            break
    return password

def Add(userID,password):
    NewRecord=userID+","+password
    file = open("Passwords.csv","a")
    file.write(str(NewRecord+"\n"))
    file.close()

def ChangePassword(tempList):
    while True:
        inlist = False
        userID =input("Enter a user ID : ")
        for row in tempList:
            if userID == row[0]:
                inlist = True
                password = NewPassword()
                row[1] = password
                break
        if inlist == True:
            break
        else:
            print("UserID isn't valid!")
    file = open("Passwords.csv","w")
    for row in tempList:
        newRecord = row[0] + ","+row[1]+"\n"
        file.write(newRecord)
    file.close()

def main():
    file = open("Passwords.csv","a")
    file.close()
    while True:
        print("\n1) Create a new User ID\n2) Change a password\n3) Display all User IDs")
        print("4) Quit\n")
        selection = input("Enter Selection: ").strip()

        tempList = GetData()
        if selection == "1":
            userID=NewUserID(tempList)
            password = NewPassword()
            Add(userID,password)
            print("New User ID added successfully!")
        elif selection == "2":
            ChangePassword(tempList)
        elif selection == "3":
            for row in tempList:
                print(row[0])
        elif selection =="4":
            break
        else:
            print("Please enter a suitable selection!!")

main ()
