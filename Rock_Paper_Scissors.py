import random
def Rock_Paper_Scissors():
    choices=["rock","paper","scissors"]

    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("Enter Your Choice:").lower()
        if player==computer:
            print("Computer:" + computer)
            print("Player:" + player)
            print("Tie")
        elif player=="rock":
            if computer=="paper":
                print("Computer:"+computer)
                print("Player:" + player)
                print("You Lose")
            if computer=="scissors":
                print("Computer:"+computer)
                print("Player:" + player)
                print("You Win")
        elif player=="paper":
            if computer=="scissors":
                print("Computer:"+computer)
                print("Player:" + player)
                print("You Lose")
            if computer=="rock":
                print("Computer:"+computer)
                print("Player:" + player)
                print("You Win")
        elif player=="scissors":
            if computer=="rock":
                print("Computer:"+computer)
                print("Player:" + player)
                print("You Lose")
            if computer=="paper":
                print("Computer:"+computer)
                print("Player:" + player)
                print("You Win")
Rock_Paper_Scissors()
while True:
    new_game=input("Want Another Game(yes/no):").lower()
    if(new_game=="yes"):
        Rock_Paper_Scissors()
    elif(new_game!="yes"):
        print("Thank you!")
        break