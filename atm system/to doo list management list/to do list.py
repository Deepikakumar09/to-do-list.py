databsePin=1234
pin=int(input("Hey Hi! Please enter your Pin..."))
if pin==databsePin:
    balance=10000
    print("###ATM Menu###")
    print("1.Check Balance")
    print("2.Deposit Amount")
    print("3.Withdraw Amount")
    print("4.Exit")
    choice=int(input("Enter your Choice please....."))
    if choice==1:
        print("Your Account Balance is: ",balance)
    elif choice==2:
        amount=int(input("Please Enter amount that you want to Deposit..."))
        balance=balance+amount
        print("Your Deposit is Successful..")
    elif choice==3:
        amount=int(input("Please Enter Amount that you want to Withdraw"))
        if amount>balance:
            print("Insufficent Balance......Sorryyy....")
        else:
            balance=balance-amount
            print("Withdraw is Successful....")
    elif choice==4:
        print("Transction is Completed....")
    else:
        print("You have Selected Invalid Option Please Check it Once again....Thank you..")
else:
    print("You have Entered Incorrect Pin..Please check it once again....Thank you")