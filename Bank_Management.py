def challenge():
    global again
    customer = int(input("Select your option \n 1. Customer Loging \n 2. New Customer \n 3. Exit"))
    CustName1 = "Arun"
    password1 = "2255"
    Amount1 = int(25000)
    
    if customer == 1:
        CustName = input("Please enter your CustName name and Password \n Cust Name: ")
        password = input("\n Password :")
        if CustName == CustName1 and password == password1:
            print(" *****Welcome  " + CustName, "*****")
            def again():
                details = input(
                    "\nAccount Details \n a.Amount Deposit \n b.Amount Withdrawal \n c.Check Balance \n d.Exit")
                if details == "a":
                    Deposit = int(input("Please enter your deposit amount "))
                    if Deposit > 0:
                        Amount = Amount1 + Deposit
                        print("Deposited Amount:-"+str(Deposit),"\n Current Balance:-" + str(Amount))
                        again()
                    else:
                        print("Please enter the valid amount ")
                elif details =="b":
                    print("Amount Withdrawal")
                elif details =="c":
                    print("Check Balance")
                elif details =="d":
                    print("Exit")
                else:
                    print("Please select the correct option")


        else:
            print("Please enter your correct CustName or Password")
    again()


challenge()






