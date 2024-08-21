import random
''' 
1 is for snake 
-1 is for water 
0 for gun
'''
computer = random.choice([-1,1,0])
you = input(" Enter your choice;-- ")
youdict = {"s":1,"w": -1,"g":0}
revdict = { 1:"snake", -1:"water", 0:"gun"}
youstr = youdict[you]

print(f"You chose{revdict[youstr]} \n computer chose {revdict[computer]}")

if( computer == youstr):
    print("Its a draw ")
else:
    if(computer == 1 and youstr == -1):
        print("You lose:(")
    elif(computer == 1 and youstr == 0):
        print("You win:)")  
    elif(computer == -1 and youstr == 0):
        print("You lose:(")    
    elif(computer == -1 and youstr == 1):
        print("You win:)") 
    elif(computer == 0 and youstr == 1):
        print("You lose:(") 
    elif(computer == 0 and youstr == -1):
        print("You win:)")   
    else :
        print("Something went wrong!!")
