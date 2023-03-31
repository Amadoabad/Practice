ABCs="abcdefghijklmnopqrstuvwxyz "

def Code(phrase,n):
    newPhrase=""
    for letter in phrase:
        Index=ABCs.index(letter)
        newIndex = Index + n
        if newIndex>26:
            newIndex =newIndex-27
        letter = ABCs[newIndex]
        newPhrase +=letter        
    return newPhrase

def Decode(codedPhrase,n):
    newPhrase=""
    for letter in codedPhrase:
        Index=ABCs.index(letter)
        newIndex = Index -n
        letter = ABCs[newIndex]
        newPhrase+=letter
    return newPhrase
while True:
    print("1)Make a code\n2)Decode a message\n3)Quit\n")
    choice = input("Enter your selection: ")
    if choice =="1":
        phrase = input("Enter a phrase: ").lower()
        num = int(input("Enter a number: "))
        print(Code(phrase,num))
    elif choice =="2":
        codedPhrase = input("Enter a phrase: ")
        num = int(input("Enter a number: "))
        print(Decode(codedPhrase,num))
    elif choice=="3":
        break
    else:
        print("Enter a suitable selection please!")
