from csv_service import CSVService #importing CSVService, to read/write data to csv
from contact import Contact #importing Contacts class to structure and query contacts

password = "Secret"
filename = "contacts.csv"
contact_list=[]
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

def option1():
    #gets requested info from user
    id = input("ID: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    company = input("Company : ")
    address = input("Address: ")
    landline = input("Landline: ")
    mobile = input("Mobile: ")
    category = input("Category: ")
    creation_date = input("Creation date : ")
    update_date = input("Todays Date: ")
    modified_by = input("Users name: ")
    #adds info to list
    new_contact =[id,fname,lname,company,address,landline,mobile,category,creation_date,update_date,modified_by]
    #adds info, as a Contact instance, to contact list
    contact_list.append(Contact(new_contact))

    print("Successfully added Contact!")

def option2():
    # search function
    print("""Please select which field you would like to search:
    1:  ID
    2:  First Name
    3:  Last Name
    4:  Company
    5:  Address
    6:  Phone (Landline)
    7:  Phone (Mobile)
    8:  Category (Development | Support | Office Fitting
    9:  Date Created
    10: Modified by (Person's Name)""")

    userinput = input("Please Enter Search Choice >>")

    if userinput == "1":
        print("ID Search Selected")
        userchoice = input("Please Enter ID >>")
        for item in contact_list:
            if item.id == userchoice:
                print(f"Match Found! - This ID Relates to {item.fname} {item.lname}")
                break
        else:
            print("No Match Found!")
    elif userinput == "2":
        print("First Name Search Selected")
    elif userinput == "3":
        print("Last Name Search Selected")
    elif userinput == "4":
        print("Company Search Selected")
    elif userinput == "5":
        print("Phone (Landline) Search Selected")
    elif userinput == "6":
        print("Phone (Landline) Search Selected")
    elif userinput == "7":
        print("Last Name Search Selected")
    elif userinput == "8":
        print("Company Search Selected")
    elif userinput == "9":
        print("Phone (Landline) Search Selected")
    elif userinput == "10":
        print("Phone (Landline) Search Selected")


def load_data():
    # using CSVService read_data method to read in contacts.csv
    instance.read_data()

    #sends list containing header to Contact object, appending to first position in contact_list
    contact_list.append(Contact(instance.header))

    #Loops through lists contained within instance.data, adding each entry as a Contact object after header in contact_list
    for data in instance.data:
        contact_list.append(Contact(data))

while True:
    #prompting user for password
    usrpswrd=input("Please enter password >>")

    if usrpswrd == password:
        print("Password Correct!")

        #calls function which reads csv file via csv_service
        #then pulls data into instances of Contacts oject and stores in contact_list
        load_data()

        while True:
            #calls on menu function
            menu()

            userinput = input(">")
            if userinput == "1":
                print("Option 1 Selected")
                option1()
            elif userinput == "2":
                print("Option 2 Selected")
                option2()
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
