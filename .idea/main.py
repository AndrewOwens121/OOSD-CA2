from csv_service import CSVService

password = "Secret"
filename = "contacts.csv"
contact_list = []

#creating an instance of the CSVService class and passing it the contacts.csv filename
instance = CSVService(filename)

def menu():
    print(f"""Please choose one of the options below:
    1) Add a Contact
    2) Search for a Contact
    3) Update a Contact
    4) Remove a Contact
    5) Search
    6) Other
    """)



while True:
    #prompting user for password
    usrpswrd=input("Please enter password >>")

    if usrpswrd == password:
        print("Correct password")
        # using CSVService read_data method to read in contacts.csv
        instance.read_data()

        while True:
            #calls on menu function
            menu()
            userinput = input(">")
            if userinput == "1":
                print("Option 1 Selected")
            elif userinput == "2":
                print("Option 2 Selected")
            elif userinput == "3":
                print("Option 3 Selected")
            elif userinput == "4":
                print("Option 4 Selected")
            elif userinput == "5":
                print("Option 5 Selected")
            elif userinput == "6":
                print("Option 6 Selected")
            else:
                print("Incorrect Choice - Please choose again")

    else:
        print("Incorrect password: Access Denied")
