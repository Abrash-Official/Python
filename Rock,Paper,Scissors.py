import random
list=["rock","paper","scissors"]
computer_choice=random.choice(list)
user_choice=input("Rock,Paper,Scissors:").lower()
if computer_choice==user_choice:
    print("It,s a Tie")
elif(
    (user_choice=="rock" and computer_choice=="scissors" ) or
    (user_choice=="paper" and computer_choice=="rock") or
    (user_choice=="scissors" and computer_choice=="paper")
):
    print("Wow!You Win")
else:
    print("Computer Win")