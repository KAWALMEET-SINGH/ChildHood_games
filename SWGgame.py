import random

SWG=["Snake","Water","Gun"]

def game(comp,you):
    if comp == you:
        return "Tie"
    elif comp == "Snake":
        if you == "Water":
            return False
        elif you == "Gun":
            return True
    elif comp == "Water":
        if you == "Gun":
            return False
        elif you == "Snake":
            return True   
    elif comp == "Gun":
        if you == "Water":
            return True
        elif you == "Snake":
            return False                 

comp=print(f"comp:{SWG} ")

a=random.randint(1,3)
if a == 1:
    comp="Snake"
elif a == 2:
    comp="Water"
else:
    comp = "Gun" 

you=input(f"Choose:{SWG}")       
print(f"COMPUTER:{comp}")
print(f"You chooose:{you}")

b=game(comp,you)
if b==True:
    print("Victory!!")
elif b==False:
    print("Lost")
else:
    print("TIE")        

   