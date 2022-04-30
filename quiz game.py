print("Welcome to  Mycomputer Quiz game")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("OKay! Let's play")
score = 0

answer=input("what does cpu stands for? ")
if answer.lower()==("central processing unit"):
    print('Correct!')
    score +=1 
else:
    print("Incorrect!")

answer=input("Who is the father of Computer science? ")
if answer.lower()==("charles babbage"):
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer=input("Scientific Name of Computer? ")
if answer.lower()==("sillico sapiens"):
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer=input("What translates and executes program at run time line by line? ")
if answer.lower()==("interpreter"):
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer=input("What converts an entire program into machine language? ")
if answer.lower()==("compiler"):
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

print("you got " + str(score)+ " questions correct")
print("you got " + str((score/5)*100) + "%.")      
if score == "100%":
    print("Great! nice job")
else:
    print("Better luck next time")    