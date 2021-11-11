from csv_service import CSVService #importing CSVService, to read/write data to csv
from contacts import Contacts #importing Contacts class to structure and query contacts

password = "Secret"
filename = "contacts.csv"
contact_list = []

#creating an instance of the CSVService class and passing it the contacts.csv filename
instance = CSVService(filename)

# mainmenu to be called multiple times
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
        print("Password Correct!")

        # using CSVService read_data method to read in contacts.csv
        instance.read_data()

        #sends list containing header to Contacts object, appending to first position in contact_list
        contact_list.append(Contacts(instance.header))
        #Loops through lists contained within instance.data, adding each entry as a Contacts object after header in contact_list
        for data in instance.data:
            contact_list.append(Contacts(data))

        # for contact in contact_list:
        #     print(contact.id)

        #while True:
            #calls on menu function

            # menu()
            # userinput = input(">")
            # if userinput == "1":
            #     print("Option 1 Selected")
            # elif userinput == "2":
            #     print("Option 2 Selected")
            # elif userinput == "3":
            #     print("Option 3 Selected")
            # elif userinput == "4":
            #     print("Option 4 Selected")
            # elif userinput == "5":
            #     print("Option 5 Selected")
            # elif userinput == "6":
            #     print("Option 6 Selected")
            #
            # else:
            #     print("Incorrect Choice - Please choose again")

    # else:
    #     print("Incorrect password: Access Denied")
