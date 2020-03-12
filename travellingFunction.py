global player
import random

def die():
    print("You died!!!")
    print ("Game Over!")

def win():
    print("You win!!!")
    print("Game Over!")

def mazeDie():
    print("You run into a giant troll")
    die()

def mazeend():
    print("You have escaped!")
    win()
    
def mazewrong():
    print("You reach a dead end")
    print("You make your way back")
    maze3()

def maze5():
    print("You continue in the maze")
    a = int(input("1 for forward. 2 for left. 3 for right."))
    if(a == 2):
        mazeend()
    else:
        mazeDie()           
def maze4():
    print("You continue in the maze")
    a = int(input("1 for forward. 2 for left. 3 for right."))
    if(a == 2):
        maze5()
    else:
        mazewrong()

def maze3():
    print("You continue in the maze")
    a = int(input("1 for forward. 2 for left. 3 for right."))
    if(a == 3):
        maze4()
    else:
        mazewrong()        

def maze2():
    print("You continue in the maze")
    a = int(input("1 for forward. 2 for left. 3 for right."))
    if(a == 1):
        maze3()
    else:
        mazewrong()
            
def light():
    print("You enter the Light")
    print("You enter a room. There is a man standing inside")
    print("'To escape you must reach the end of the maze' he says")
    print("You are at the start of a maze")
    a = int(input("1 for forward. 2 for left. 3 for right."))
    if(a == 1):
        maze2()
    else:
        mazeDie()
          
def fight1():
    a = random.randint(1,2)
    if(a == 1):
        print("You manage to overpower him")
        print("'Don't enter the light' he says.")
        light()
    else:
        print("He was too strong!")
        die()

def run1():
    a = random.randint(1,5)
    if(a <= 2):
        print("You manage to keep away.You sneak around and go back to the light")
        light()
    else:
        print("He was too fast!")
        die()

def fight2():
    a = random.randint(1,5)
    if(a == 1):
        print("You manage to overpower him")
        win()
    else:
        print("He was too strong!")
        die()
def fight3():
    a = random.randint(1,2)
    if(a == 1):
        print("You manage to overpower him")
        win()
    else:
        print("He was too strong!")
        die()
        
    
def find():
    print("You found a knife")
    print("There are two doors.")
    a = int(input("1 for left two for right"))
    if(a == 1):
        print("There is nothing behind the door. You fall to your death")
        die()
    if(a == 2):
        fight3()
    
def fights():
    print("You see a 2 doors")
    a = input(input("1 for right. 2 for left."))
    if(a == 1):
        print("You are attacked")
        fight2()
    elif(a == 2):
        find()
        
        

def back():
    print("You go home. The end.")

def up():
    print("There are two doors.")
    a = int(input("1 for left two for right"))
    if(a == 1):
        print("There is nothing behind the door. You fall to your death")
        die()
    if(a == 2):
        fights()
    elif(a == 3):
        print("You found the secret end!")          
        win()              

def inside():
    print("You a staircase going up and one going down. Where do you go?")
    a = int(input("1 for up. 2 for down."))
    if(a == 1):
        up()
    if(a == 2):
        down()

def outside():
    print("You walk around to the back of the house and towards the woods behind the house.")
    print("You walk in and see a light coming from the distance You go in")
    print("You see a man standing gaurd. He lunges at you")
    a = int(input("1 to fignt 2 to run"))
    if(a == 1):
        fight1()
    if(a == 2):
        run1()
    

def start():
    print("You come to a house in the middle of an empty field. Where do you go?")
    print("1 to go inside")
    print("2 to walk around the house")
    print("3 to go away")
    b = int(input("Which one? "))
    if(b == 1):
        inside()
    elif(b == 2):
        outside()
    elif(b == 3):
        back()


player = input("What is your name? ")
print(f"Hello {player}")
start()    
