

#HAVE TO CHANGE THE WHOLE THING!!!!!!!!!!!!!!!









print("Enter 1 to get the product information") #A
print("Enter 2 to request a quotation") #B
print("Enter 3 to locate a dealer near you") #C
print("Enter 4 to connect with customer support call centre") #D
print("Enter 5 to know about schemes") #E

choice = int(input("Enter your choice: 1, 2, 3, 4 or 5: "))
if choice == 1:
    print("Select our product range by entering an appropriate product choice from 6, 7 or 8! ") #A1
    print("Enter 6 for Cranes")
    print("Enter 7 for BHL")
    print("Enter 8 for Compactors")
    
    product = int(input("Enter the product choice as 6, 7 or 8: "))

    if product == 6:
        print("Select the cranes model by entering the choice of the model")
        print("Enter A for model Digmax II (2WD)")
        print("Enter B for model Digmax II (4WD)")
        print("Enter C for model Loadgmax II")
        model = input("Enter the model choice as A, B or C: ")
        if model == "A":
            print("Here is the pdf link for model Digmax II (2WD)")
            print("https://www.escortsgroup.com/")
        elif model == "B":
            print("Here is the pdf link for model Digmax II (4WD)")
            print("https://www.escortsgroup.com/")
        elif model == "C":
            print("Here is the pdf link for model Loadgmax II")
            print("https://www.escortsgroup.com/")

            

    elif product == 7:
        print("Select the BHL model by entering the choice of the model")
        print("Enter P for model Digmax II (2WD)")
        print("Enter Q for model Digmax II (4WD)")
        print("Enter R for model Loadgmax II")
        model = input("Enter the model choice as P, Q or R: ")
        if model == "P":
            print("Here is the pdf link for model Digmax II (2WD)")
            print("https://www.escortsgroup.com/")
        elif model == "Q":
            print("Here is the pdf link for model Digmax II (4WD)")
            print("https://www.escortsgroup.com/")
        elif model == "R":
            print("Here is the pdf link for model Loadgmax II")
            print("https://www.escortsgroup.com/")



    elif product == 8:
        print("Select the compactors model by entering the choice of the model")
        print("Enter X for model Digmax II (2WD)")
        print("Enter Y for model Digmax II (4WD)")
        print("Enter Z for model Loadgmax II")
        model = input("Enter the model choice as X, Y or Z: ")
        if model == "X":
            print("Here is the pdf link for model Digmax II (2WD)")
            print("https://www.escortsgroup.com/")
        elif model == "X":
            print("Here is the pdf link for model Digmax II (4WD)")
            print("https://www.escortsgroup.com/")
        elif model == "Z":
            print("Here is the pdf link for model Loadgmax II")
            print("https://www.escortsgroup.com/")

        
    

elif choice == 2:#A2
    print("Please fill the following information using URL")
    print("https://www.escortsgroup.com/")


elif choice == 3:#A3
    print("Kindly share your current location using WhatsApp or SMS")
    print("Send a message with your state name through SMS to 9999999999")
    print("Or share your location using WhatsApp location service")
    print("We will share details of dealer with name, address, and contact number! ")


elif choice == 4:#A4
    print("Our toll free number is 1800-180-4488")
    print("Our representative will connect with you soon!")


elif choice == 5:#A5
    print("Sharing the URL below for the scheme")
    print("https://www.escortsgroup.com/")


    
else:
    print("Please enter a valid choice from 1, 2, 3, 4 or 5!")












    
    
