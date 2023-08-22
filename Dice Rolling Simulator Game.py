import random2

def roll_num():
    return random2.randint(1,6)

def dice_role():
    score = 0
    while True:
        select = input("do u want to role the dice? (y/n)")
        if select.lower()=="y":
            print(roll_num())
            score+=roll_num()
            print("ur score is",score)
        else:
            select = input("do u want to quit? (y/n)")
            if select.lower()=="y":
                break
            else:
                continue
print("lets start the match")

dice_role()

