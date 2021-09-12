print("Welcome to Neo Bank ATM :")
restart = "y"
chances = 3
balance = 200.48
while chances >= 0:
    pin = int(input("Please Enter your Pin : "))
    if pin == 1234:
        print("Your Entered pin is Correct \n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Press 1 for Balance Enquire : \n ")
            print("Press 2 for Withdrawal : \n ")
            print("Press 3 for To Pay Amount : \n ")
            print("Press 4 for Return Card : \n ")
            option = int(input("What would you like to Choose ? "))
            if option == 1:
                print("Your Balance is ", balance, '\n')
                restart = input("Would you like to go back ? ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You , Revisit Again ! ")
                    break
            elif option == 2:
                option2 = "y"
                withdrawal = float(input("How much money would you like to withdrawal \n $10 /$20 /$40 /$60 /$80 /$100 : "))
                if withdrawal in [10, 20, 40, 60, 80, 100, 1000, 5000]:
                    balance = balance - withdrawal
                    print("\n Your Balance is now :", balance)
                    restart = input("would you like to go Back ? ")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("Thanks you Revisit Again ! ")
                        break
            elif option == 3:
                pay_in = float(input("How much money would you like to pay-in :"))
                balance = balance + pay_in
                print("\n Your Balance is now ", balance)
                restart = input("Would you like to go go back ?")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank you , revisit Again !")
                    break
            elif option == 4:
                print('Please Wait Wiliest your Card is returned ... \n')
                print("Thanks you for your service ")
                break
        else:
            print("Please enter Correct Number \n ")
            restart = "Y"
    elif pin != '1234':
        print("Incorrect Password ")
        chances = chances - 1
        if chances == 0:
            print("\n No more Tries ")
            break
