from csv_service import CSVService  # importing CSVService, to read/write data to csv
from contact import Contact  # importing Contacts class to structure and query contacts
import time #Time imported to add delays

password = "Secret"
filename = "contacts.csv"
contact_list = []
write_list = []
# creating an instance of the CSVService class and passing it the contacts.csv filename
instance = CSVService(filename)


# mainmenu to be called multiple times
def menu():
    clear_screen()
    print(f"""Please choose one of the options below:
    1) Add a Contact
    2) Search for a Contact
    3) Update a Contact
    4) Remove a Contact
    5) Reports
    0) Exit
    """)


# Add Contact Function
def option1():
    """
    Function to add a new contact to the database
    :return:
    """

    print("Please Enter the New Contacts Details as prompted")

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
    # adds info to list
    new_contact = [id, fname, lname, company, address, landline, mobile, category, creation_date, update_date,
                   username]
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
    clear_screen()

    # ID Search Below
    if userinput == "1":
        print("ID Search Selected")
        userchoice = input("Please Enter ID >>")
        for item in contact_list:
            if item.id == userchoice:
                print(
                    f"Match Found!\nID: {item.id}\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # First Name Search below
    elif userinput == "2":
        print("First Name Search Selected")
        userchoice = input("Please Enter First Name >>")
        for item in contact_list:
            if item.fname == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Last Name Search below
    elif userinput == "3":
        print("Last Name Search Selected")
        userchoice = input("Please Enter last Name >>")
        for item in contact_list:
            if item.lname == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Company Search Below
    elif userinput == "4":
        print("Company Search Selected")
        userchoice = input("Please Enter Company Name >>")
        for item in contact_list:
            if item.company == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Address Search Below
    elif userinput == "5":
        print("Address Search Selected")
        userchoice = input("Please Enter Address >>")
        for item in contact_list:
            if item.address == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Landline Search Below
    elif userinput == "6":
        print("Phone (Landline) Search Selected")
        userchoice = input("Please Enter Address >>")
        for item in contact_list:
            if item.landline == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Mobile Search Below
    elif userinput == "7":
        print("Mobile Phone Search Selected")
        userchoice = input("Please Enter Mobile Number >>")
        for item in contact_list:
            if item.mobile == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Category Search Seleted
    elif userinput == "8":
        print("Category Search Selected")
        userchoice = input("Please Enter Category >>")
        for item in contact_list:
            if item.category == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Creation Date Search
    elif userinput == "9":
        print("Creation Date Search Selected")
        userchoice = input("Please Enter Category >>")
        for item in contact_list:
            if item.reation_date == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Update Date Search
    elif userinput == "10":
        print("Update Date Search Selected")
        userchoice = input("Please Enter Update Date >>")
        for item in contact_list:
            if item.update_date == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)

    # Update Date Search
    elif userinput == "11":
        print("Modified By Search Selected")
        userchoice = input("Please Enter Username >>")
        for item in contact_list:
            if item.modified_by == userchoice:
                print(
                    f"Match Found!\nFull Name: {item.fname} {item.lname}\n| Company : {item.company} | Mobile :{item.mobile} | Landline:{item.landline} |")
                time.sleep(4)
                break
        else:
            print("No Match Found!")
            time.sleep(2)


# Edit/Update Function
def option3():
    # Taking in ID of targetted contact from user
    userID = input("Please Enter the ID of the Record to be Updated: ")

    # Searching list, to find record matching UserID - Storing pointer to that record in temp variable
    for con in contact_list:
        if userID == con.id:
            temp = con
            print(f"User '{con.fname} {con.lname}' Selected")
            time.sleep(2)
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
    0:  Main Menu""")

    # Taking user's input of selection
    user_choice = input(">>")

    # Actioning the users selection with Setters in Contact Class
    if user_choice == "1":
        edit = input("Please Enter The New Value: ")
        temp.set_id(edit)
        temp.set_modified_by(username)

    elif user_choice == "2":
        edit = input("Please Enter The New Value: ")
        temp.set_fname(edit)
        temp.set_modified_by(username)

    elif user_choice == "3":
        edit = input("Please Enter The New Value: ")
        temp.set_lname(edit)
        temp.set_modified_by(username)

    elif user_choice == "4":
        edit = input("Please Enter The New Value: ")
        temp.set_company(edit)
        temp.set_modified_by(username)

    elif user_choice == "5":
        edit = input("Please Enter The New Value: ")
        temp.set_address(edit)
        temp.set_modified_by(username)

    elif user_choice == "6":
        edit = input("Please Enter The New Value: ")
        temp.set_landline(edit)
        temp.set_modified_by(username)

    elif user_choice == "7":
        edit = input("Please Enter The New Value: ").strip()
        temp.set_mobile(edit)
        temp.set_modified_by(username)

    elif user_choice == "8":
        edit = input("Please Enter The New Value: ")
        temp.set_category(edit)
        temp.set_modified_by(username)

    elif user_choice == "9":
        edit = input("Please Enter The New Value: ")
        temp.set_creation_date(edit)
        temp.set_modified_by(username)

    elif user_choice == "10":
        edit = input("Please Enter The New Value: ")
        temp.set_update_date(edit)
        temp.set_modified_by(username)


    # Invalid input and 0 - Returns to Main Menu
    else:
        print("Invalid Input!")


# Remove Record Function
def option4():
    # Taking in ID of targetted contact from user
    userID = input("Please Enter the ID of the Record to be Removed: ")

    # Searching list, to find record matching UserID - Storing pointer to that record in temp variable
    for con in contact_list:
        if userID == con.id:
            temp = con
            print(f"User '{con.fname} {con.lname}' Selected")
            break
    else:
        print("User ID not found")

    # Verifying that the Record selected is to be deleted
    answer = input("Is this the User you wish to Remove? Type yes/no").lower()

    if answer == "yes":
        # Removing selected record from contact_list
        contact_list.remove(temp)
    else:
        print("Please Choose another ID - Use the search function to find ID choice")


# Reports Function
def option5():

    # Initialises empty list to add contacts to
    display_list = []

    # Sub-Menu
    userinput = input("""Choose Report:
    1: Full List of Contacts
    2: List of Development Contacts
    3: List of Support Contacts
    4: List of Office Fitting Contacts\n>""")

    # Conditionals to choose which report to run
    if userinput == "1":
        for contact in contact_list:
            print(contact.get_full_detail())

    if userinput == "2":
        print("Development Category List:")
        for contact in contact_list:
            if contact.get_category() == "Development":
                display_list.append(contact)
                print(vars(contact))

    if userinput == "3":
        print("Support Category List:")
        for contact in contact_list:
            if contact.get_category() == "Support":
                display_list.append(contact)
                print(vars(contact))

    if userinput == "4":
        print("Support Office Fitting List:")
        for contact in contact_list:
            if contact.get_category() == "Office Fitting":
                display_list.append(contact)
                print(vars(contact))


#Exit Function
def option6():
    userinput=input("""***Exit Selected***
    Would you like to save your work? Y/N""").lower()

    if userinput == "y":
        write_data()
        print("Saved Successfully!")
    else:
        print("Exit - Unsaved")


# Function to Read/Write to CSV file
def load_data():
    # using CSVService read_data method to read in contacts.csv
    instance.read_data()

    # sends list containing header to Contact object, appending to first position in contact_list
    contact_list.append(Contact(instance.header))

    # Loops through lists contained within instance.data, adding each entry as a Contact object after header in contact_list
    for data in instance.data:
        contact_list.append(Contact(data))

# Function to Write to CSV faile
def write_data():

    for contact in contact_list:
        temp=[contact.get_id(),contact.get_fname(),contact.get_lname(),contact.get_company(),contact.get_address(),contact.get_landline(),contact.get_mobile(),contact.get_category(),contact.get_creation_date(),contact.get_update_date(),contact.get_modified_by()]
        write_list.append(temp)
    # using CSVService read_data method to read in contacts.csv
    instance.write_data(write_list)


def clear_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n")

# Main Code
while True:

    #prompting user for username
    username = input("Please enter your username >>")

    # prompting user for password
    usrpswrd = input("Please enter password >>")

    # checking user input against hardcoded password
    if usrpswrd == password:
        print("Password Correct!")
        time.sleep(2)
        clear_screen()

        # calls function which reads csv file via csv_service
        # then pulls data into instances of Contacts oject and stores in contact_list
        load_data()

        while True:
            # calls on menu function
            menu()

            userinput = input(">")
            if userinput == "1":
                print("'Add a Contact' Selected")
                time.sleep(2)
                clear_screen()
                option1()
            elif userinput == "2":
                print("'Search for a Contact' Selected")
                time.sleep(2)
                clear_screen()
                option2()
            elif userinput == "3":
                print("'Update a Contact' Selected")
                time.sleep(2)
                clear_screen()
                option3()
            elif userinput == "4":
                print("'Remove a Contact' Selected")
                time.sleep(2)
                clear_screen()
                option4()
            elif userinput == "5":
                print("'Reports' Selected")
                time.sleep(2)
                clear_screen()
                option5()
            elif userinput == "0":
                print("'Exit' Selected")
                time.sleep(2)
                clear_screen()
                option6()

            else:
                print("Incorrect Choice - Please choose again")

    else:
        print("Incorrect password: Try Again")
