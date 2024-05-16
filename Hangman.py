from turtle import *
import random

pensize(10)
pencolor("black")
penup()
goto(300,-400)
pendown()
goto(300,250)
goto(0,250)
goto(0,200)
penup()



guess=['varchasva','coding']
x=True
c=0
words="aeiou"
w=""
a=input("Start y/n")

if a=='y':
    g=random.choice(guess)
    for i in g:
        if i in words:
            print(i,end=" ")
        else:            
            print('_',end=" ")

while x:
    print("\n guess the Word letter by letter ")
    a=input("Guess:  ")
    w+=a
    if w==g:
        print("You Won ^--^")        
    if a==" " or a=="":
        print('Blank is not a guess')
    elif a.lower() in words:
        print("Letter is already there -_-")
    elif a.lower() in g:
        words+=a.lower()
        print("Thats Correct")
        for i in g:
            if i in words:
                print(i,end=" ")
            else:            
                print('_',end=" ")
    
    else:
        print("Wrong")
        if c==0:            
            pensize(10)
            pencolor("cyan")
            goto(0,0)
            circle(100)
        elif c==1:
            pensize(10)
            pencolor("cyan")
            penup()
            goto(0,0)
            pendown()
            goto(0,-200)
        elif c==2:
            goto(-100,-300)
            penup()
            goto(0,-200)
        elif c==3:
            pendown()
            goto(100,-300)
            penup()
            goto(0,-100)
        elif c==4:
            pendown()
            goto(-100,-200)
            penup()
            goto(0,-100)
        elif c==5:
            pendown()
            goto(100,-200)
        elif c==6:
            print("Game Over")
            break
        c+=1

            
            
        

    
                
    
