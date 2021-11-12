from csv_service import CSVService  # importing CSVService, to read/write data to csv
from contact import Contact  # importing Contacts class to structure and query contacts

password = "Secret"
filename = "contacts.csv"
contact_list = []
# creating an instance of the CSVService class and passing it the contacts.csv filename
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

# Add Contact Function
def option1():
    """
    Function to add a new contact to the database
    :return:
    """
    # gets requested info from user
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
    # adds info to list
    new_contact = [id, fname, lname, company, address, landline, mobile, category, creation_date, update_date,
                   modified_by]
    # adds info, as a Contact instance, to contact list
    contact_list.append(Contact(new_contact))

    print("Successfully added Contact!")

# Search Contact Function
def option2():
    """
    Function to Search Contact_list for user input covering all fields
    :return: Confirmation of Record existing - and some other of the Records data (depending on search type)
    """
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

    #ID Search Below
    if userinput == "1":
        print("ID Search Selected")
        userchoice = input("Please Enter ID >>")
        for item in contact_list:
            if item.id == userchoice:
                print(
                    f"Match Found!\nID: {item.id}\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # First Name Search below
    elif userinput == "2":
        print("First Name Search Selected")
        userchoice = input("Please Enter First Name >>")
        for item in contact_list:
            if item.fname == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Last Name Search below
    elif userinput == "3":
        print("Last Name Search Selected")
        userchoice = input("Please Enter last Name >>")
        for item in contact_list:
            if item.lname == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Company Search Below
    elif userinput == "4":
        print("Company Search Selected")
        userchoice = input("Please Enter Company Name >>")
        for item in contact_list:
            if item.company == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Address Search Below
    elif userinput == "5":
        print("Address Search Selected")
        userchoice = input("Please Enter Address >>")
        for item in contact_list:
            if item.address == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Landline Search Below
    elif userinput == "6":
        print("Phone (Landline) Search Selected")
        userchoice = input("Please Enter Address >>")
        for item in contact_list:
            if item.landline == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Mobile Search Below
    elif userinput == "7":
        print("Mobile Phone Search Selected")
        userchoice = input("Please Enter Mobile Number >>")
        for item in contact_list:
            if item.mobile == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Category Search Seleted
    elif userinput == "8":
        print("Category Search Selected")
        userchoice = input("Please Enter Category >>")
        for item in contact_list:
            if item.category == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Creation Date Search
    elif userinput == "9":
        print("Creation Date Search Selected")
        userchoice = input("Please Enter Category >>")
        for item in contact_list:
            if item.reation_date == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Update Date Search
    elif userinput == "10":
        print("Update Date Search Selected")
        userchoice = input("Please Enter Update Date >>")
        for item in contact_list:
            if item.update_date == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

    # Update Date Search
    elif userinput == "11":
        print("Modified By Search Selected")
        userchoice = input("Please Enter Username >>")
        for item in contact_list:
            if item.modified_by == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                break
        else:
            print("No Match Found!")

# Edit/Update Function
def option3():
    #Taking in ID of targetted contact from user
    userID=input("Please Enter the ID of the Record to be Changed: ")

    # Searching list, to find record matching UserID - Storing pointer to that record in temp variable
    for con in contact_list:
        if userID == con.id:
            temp = con
            print(f"User {con.fname} {con.lname} Selected")
            break
    else:
        print("User ID not found")

    # Printing List of Editable attributes
    print("""Please select which field you would like to edit:
    1:  ID
    2:  First Name
    3:  Last Name
    4:  Company
    5:  Address
    6:  Phone (Landline)
    7:  Phone (Mobile)
    8:  Category (Development | Support | Office Fitting
    9:  Date Created
    10: Update Date
    11: Modified by (Person's Name)
    0:  Main Menu""")

    #Taking user's input of selection
    user_choice = input(">>")

    #Actioning the users selection with Setters in Contact Class
    if user_choice == "1":
        edit = input("Please Enter The New Value: ")
        temp.set_id(edit)

    elif user_choice == "2":
        edit = input("Please Enter The New Value: ")
        temp.set_fname(edit)

    elif user_choice == "3":
        edit = input("Please Enter The New Value: ")
        temp.set_lname(edit)

    elif user_choice == "4":
        edit = input("Please Enter The New Value: ")
        temp.set_company(edit)

    elif user_choice == "5":
        edit = input("Please Enter The New Value: ")
        temp.set_address(edit)

    elif user_choice == "6":
        edit = input("Please Enter The New Value: ")
        temp.set_landline(edit)

    elif user_choice == "7":
        edit = input("Please Enter The New Value: ")
        temp.set_mobile(edit)

    elif user_choice == "8":
        edit = input("Please Enter The New Value: ")
        temp.set_category(edit)

    elif user_choice == "9":
        edit = input("Please Enter The New Value: ")
        temp.set_creation_date(edit)

    elif user_choice == "10":
        edit = input("Please Enter The New Value: ")
        temp.set_update_date(edit)

    elif user_choice == "11":
        edit = input("Please Enter The New Value: ")
        temp.set_modified_by(edit)

    # Invalid input and 0 - Returns to Main Menu
    else:
        print("Invalid Input!")

def load_data():
    # using CSVService read_data method to read in contacts.csv
    instance.read_data()

    # sends list containing header to Contact object, appending to first position in contact_list
    contact_list.append(Contact(instance.header))

    # Loops through lists contained within instance.data, adding each entry as a Contact object after header in contact_list
    for data in instance.data:
        contact_list.append(Contact(data))


while True:
    # prompting user for password
    usrpswrd = input("Please enter password >>")

    # checking user input against hardcoded password
    if usrpswrd == password:
        print("Password Correct!")

        # calls function which reads csv file via csv_service
        # then pulls data into instances of Contacts oject and stores in contact_list
        load_data()

        while True:
            # calls on menu function
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
                option3()
            elif userinput == "4":
                print("Option 4 Selected")
            elif userinput == "5":
                print("Option 5 Selected")
            elif userinput == "6":
                print("Option 6 Selected")

            else:
                print("Incorrect Choice - Please choose again")

    else:
        print("Incorrect password: Try Again")
