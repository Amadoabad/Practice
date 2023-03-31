from random import choice

colours=["red","blue","green","yellow","black","brown"]
def GeneratedColours():
    answer=[]
    for i in range(4):
        colour=choice(colours)
        answer.append(colour)
    return answer

def GettingGuesses():
    while True:
        print(colours)
        guess=input("Please guess the 4 colours in the right sequence: ").split()
        if len(guess)==4:
            break
        else:
            print("Enter 4 colours from the list above please: ")
    return guess

def Comparing(answer,guess):
    tempAnswer=list(answer)
    tempGuess=list(guess)
    CC = 0 # Correct colour Correct place
    CW = 0 # Correct colour Worng place
    x=-1
    for i in tempGuess:
        x+=1
        if i == tempAnswer[x]:
            CC +=1
            tempGuess[x] ="checked"
            tempAnswer[x] ="checked"
            

    for i in tempGuess:
        if i in tempAnswer and i != "checked":
            temp = tempAnswer.index(i)
            tempAnswer[temp] = "checked"
            CW+=1
            
    score=(CC,CW)
    return score
    
def main():
    answer = GeneratedColours()
    tries =0
    while True:
        tries+=1
        guess = GettingGuesses()
        score=Comparing(answer,guess)
        print("Correct colour in the correct place:",score[0])
        print("Correct colour in the wrong place:",score[1])
        if score[0]==4:
            break
    print("You did it!")
    print("It took you",tries,"tries to finish!")
    input()
main()