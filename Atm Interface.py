print("Hello! Welcome to our Atm")
pin=["7896",'1234','0987','0879']
balance= 50000
atempt=0
while True:

    # Don't Enough Money

    if balance <500:
        print("You don't have enough money!!!")
    
    # # atempts

    # atempt+=1
    # if (atempt==4):
    #     print("Maximum trial reached!")
    #     break

    #user pin

    upin=(str(input("Enter your pin Sir!: ")))
    if (upin in pin):

        #options

        print("Welcome Sir!\n1:Cash Withdraw        2:Fast Cash\n3:Balance Check       4:Cash Deposite\n5:Cancle")
        option=(str(input("Your Option: ".lower())))

        #If option 1 = Cash Withdraw

        if (option=='1' or option== "Cash Withdraw"):
            cashw=int(input("Enter a amount which is multiple of 500\nMin-Amount=500        Max-Amount=20000\nEnter Cash to withdraw Sir: "))
            if (cashw%500 == 0 and cashw>=500 and cashw<=20000):
                print(f"Here is your cash {cashw} Sir!ThankYou for visiting our Atm")
                balance=balance-cashw
            elif(cashw % 500 != 0):
                print("Try a value which is multiple of 500!")

        #If option 2 = Fash Cash

        elif (option=='2' or option=='Fast Cash'):
            fashC=input('A:500      B:1000\nC:2000      D:3000\nE:4000      F:5000\nEnter your option Sir: ').lower()
            if fashC=="a":
                print(f'Here is your cash {500} Sir!')
                balance=balance-500
            if fashC=="b":
                print(f'Here is your cash {1000} Sir!')
                balance=balance-1000
            if fashC=="c":
                print(f'Here is your cash {2000} Sir!')
                balance=balance-2000
            if fashC=="d":
                print(f'Here is your cash {3000} Sir!')
                balance=balance-3000
            if fashC=="e":
                print(f'Here is your cash {4000} Sir!')
                balance=balance-4000
            if fashC=="f":
                print(f'Here is your cash {5000} Sir!')
                balance=balance-5000

        #If option 3 = Balance Check

        elif (option=='3'):
            print(f'Your balance is {balance}Pkr')

        # if option 4 = Cash Deposite

        elif (option=='4' or option=="Cash Deposite"):
            cashD=int(input('Enter your Cash which you wnat to deposite: '))
            balance=balance+cashD

        # If Option 5 = Cancles

        elif (option=='5' or option=='Cancle'):
            print('Bye Bye')
            break

    else:
        print("Try Again!".center(30))