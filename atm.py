GTB = 1
AccessBank = 2
FirstBank = 3
ZenithBank = 4
print ("_________________________________________________")
print ("******************Select Bank**********************")
print ("_________________________________________________")
print ("1 - GTB", "2 - Access Bank", "3 - First Bank", "4 - Zenith Bank")
Bankname = int(input("Select Bank: "))

if Bankname == 1:
    print("Welcome to Guaranty Trust Bank")

elif Bankname == 2:
    print("Welcome to Access Bank")

elif Bankname == 3:
    print("Welcome to First Bank")

elif Bankname == 4:
    print("Welcome to Zenith Bank")

print("Please Enter your PIN number")
Pin = int(input("Enter Pin: "))

if Pin == 0000:
    print ("_________________________________________________")
    print ("******************Welcome to our Bank**********************")
    print ("_________________________________________________")
else:
    print ("_________________________________________________")
    print ("********************incorrect pin entry********************")
    print ("_________________________________________________")

WithdrawCash = 5
AboutmyAccount = 6
Transfer = 7
ChangePin = 8
print ("5 - WithdrawCash", "6 - AboutmyAccount","7 - Transfer","8 - ChangePin")


Transaction = int(input("Select Transaction: "))



if Transaction == 5:
    amount = int(input("Enter Amount to withdraw: "))
    denomination = 1000     #meaning notes available to be withdrawn on ATM
    r =  amount//denomination

    print ("....Processing, Please wait!")
    print ("Take your cash")
    for amount in range (0,r):
        print (denomination)


        
elif Transaction == 6:
    print ("Your account balance is One Million, two hundred and twenty thousand naira only")
    print ("")
    '''
    print ("Would you want to perform other transction")
    Sure = 1
    Nope = 2
    print ("1 -yes or 2 -no")
    Response = int(input("Please Choose Options:"))
    if Response == 1:
        print("Please Enter your PIN number:")
        print ("5 - WithdrawCash", "6 - AboutmyAccount","7 - Transfer","8 - ChangePin")
        Transaction = int(input("Select Transaction: "))
    else:
    '''
    print ("Thank you for banking with us")
    print("")
    print ("Take your card")
    

elif Transaction == 7:
    print ("_________________________________________________")
    print ("******************Welcome to our Bank**********************")

    receiver = int(input("Enter receiver's NUBAN: "))

    GTB = 1
    AccessBank = 2
    FirstBank = 3
    ZenithBank = 4
print ("_________________________________________________")
print ("******************Select Bank**********************")
print ("_________________________________________________")
print ("1 - GTB", "2 - Access Bank", "3 - First Bank", "4 - Zenith Bank")
Bankname = int(input("Select Bank: "))

if Bankname == 1:
    print("Select Bank is Gurantee Trust Bank")

elif Bankname == 2:
    print("Select Bank is Access Bank")

elif Bankname == 3:
    print("Select Bank is First Bank")

elif Bankname == 4:
    print("Select Bank is Zenith Bank")

elif Transaction == 8:
    old = int (input("Enter Old pin: "))
    new = int(input("Enter New pin: "))
    print("pin changed successfully!!!")
    print("")
    print("Thank you for banking with us!")
    

