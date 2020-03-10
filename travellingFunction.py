global player

    
def back():
    print("You go home. The end.")

def inside():
    print("You a staircase going up and one going down. Where do you go?")
    a = input("1 for up. 2 for down.")
    if(a == 1):
        up()
    if(a == 2):
        down()
    

def start():
    print("You come to a house in the middle of an empty field. Where do you go?")
    print("1 to go inside")
    print("2 to walk around the house")
    print("3 to go away")
    b = input("Which one?")
    if(b == 1):
        inside()
    elif(b == 2):
        outside()
    elif(b == 3):
        back()

def intro():
    player = input("What is your name?")
    print(f"Hello {player}")
    start()    

intro()
