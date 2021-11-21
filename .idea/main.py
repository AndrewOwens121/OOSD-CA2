from csv_service import CSVService  # importing CSVService, to read/write data to csv
from contact import Contact  # importing Contacts class to structure and query contacts
import time  # Time imported to add delays
from datetime import date

# initilising variables and lists
password = "Secret"
filename = "contacts.csv"
current_id = 0
contact_list = []
write_list = []

# creating an instance of the CSVService class and passing it the contacts.csv filename
instance = CSVService(filename)



def menu():
    """
    Function to display the main menu
    :return:
    """
    clear_screen()
    print(f"""Please choose one of the options below:
    1) Add a Contact
    2) Search for a Contact
    3) Update a Contact
    4) Remove a Contact
    5) Reports
    0) Exit
    """)


def option1(current_id):
    """
    Function to add a new contact to the database
    :return:
    """

    print("Please Enter the New Contacts Details as prompted")

    # gets requested info from user
    fname = input("First Name: ")
    lname = input("Last Name: ")
    company = input("Company : ")
    address = input("Address: ")
    landline = input("Landline: ")
    mobile = input("Mobile: ")

    # Entry for Category diverts from normal, as Category needs to be choice of 3 options only
    choice = input("""Category:
     1) Development
     2) Office Fitting
     3) Support
     >>""")

    if choice == "1":
        category = "Development"
    elif choice == "2":
        category = "Office Fitting"
    elif choice == "3":
        category = "Support"
    else:
        print("Incorrect Entry! Exiting to main menu")
        time.sleep(2)
        return

    # adds info to list
    new_contact = [current_id, fname, lname, company, address, landline, mobile, category, date.today(), date.today(),
                   username]
    # adds info, as a Contact instance, to contact list
    contact_list.append(Contact(new_contact))

    # increments current_id variable
    current_id += 1

    print("Successfully added Contact!")
    time.sleep(2)


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

        temp = []

        print("ID Search Selected")
        userchoice = input("Please Enter ID >>")

        for item in contact_list:
            if item.id == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # First Name Search below
    elif userinput == "2":

        temp = []

        print("First Name Search Selected")
        userchoice = input("Please Enter First Name >>")

        for item in contact_list:
            if item.get_fname() == userchoice:
                temp.append(item.get_full_detail())

        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Last Name Search below
    elif userinput == "3":

        temp = []

        print("Last Name Search Selected")
        userchoice = input("Please Enter last Name >>")
        for item in contact_list:
            if item.lname == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Company Search Below
    elif userinput == "4":

        temp = []

        print("Company Search Selected")
        userchoice = input("Please Enter Company Name >>")
        for item in contact_list:
            if item.company == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{temp}")
            time.sleep(5)

    # Address Search Below
    elif userinput == "5":

        temp = []

        print("Address Search Selected")
        userchoice = input("Please Enter Address >>")
        for item in contact_list:
            if item.address == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{temp}")
            time.sleep(5)

    # Landline Search Below
    elif userinput == "6":

        temp = []

        print("Phone (Landline) Search Selected")
        userchoice = input("Please Enter Address >>")
        for item in contact_list:
            if item.landline == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Mobile Search Below
    elif userinput == "7":

        temp = []

        print("Mobile Phone Search Selected")
        userchoice = input("Please Enter Mobile Number >>")
        for item in contact_list:
            if item.mobile == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Category Search Seleted
    elif userinput == "8":

        temp = []

        print("Category Search Selected")
        userchoice = input("Please Enter Category >>")
        for item in contact_list:
            if item.category == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Creation Date Search
    elif userinput == "9":

        temp = []

        print("Creation Date Search Selected")
        userchoice = input("Please Enter Category >>")
        for item in contact_list:
            if item.reation_date == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Update Date Search
    elif userinput == "10":

        temp = []

        print("Update Date Search Selected")
        userchoice = input("Please Enter Update Date >>")
        for item in contact_list:
            if item.update_date == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)

    # Update Date Search
    elif userinput == "11":

        temp = []

        print("Modified By Search Selected")
        userchoice = input("Please Enter Username >>")
        for item in contact_list:
            if item.modified_by == userchoice:
                temp.append(item.get_full_detail())
        if len(temp) == 0:
            print("No Match Found!")
            time.sleep(2)

        else:
            print("Match Found!")
            for t in temp:
                print(f"{t}")
            time.sleep(5)


def option3():
    """
    Function to Update/Edit records, records are selected via ID confirmation - provided by user input - edited via setters
    :return: None
    """
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
    1:  First Name
    2:  Last Name
    3:  Company
    4:  Address
    5:  Phone (Landline)
    6:  Phone (Mobile)
    7:  Category (Development | Support | Office Fitting
    0:  Main Menu""")

    # Taking user's input of selection
    user_choice = input(">>")

    # Actioning the users selection with Setters in Contact Class
    if user_choice == "1":
        edit = input("Please Enter The New Value: ")
        temp.set_fname(edit)
        temp.set_update_date(date.today())
        temp.set_modified_by(username)

    elif user_choice == "2":
        edit = input("Please Enter The New Value: ")
        temp.set_lname(edit)
        temp.set_update_date(date.today())
        temp.set_modified_by(username)

    elif user_choice == "3":
        edit = input("Please Enter The New Value: ")
        temp.set_company(edit)
        temp.set_update_date(date.today())
        temp.set_modified_by(username)

    elif user_choice == "4":
        edit = input("Please Enter The New Value: ")
        temp.set_address(edit)
        temp.set_update_date(date.today())
        temp.set_modified_by(username)

    elif user_choice == "5":
        edit = input("Please Enter The New Value: ")
        temp.set_landline(edit)
        temp.set_update_date(date.today())
        temp.set_modified_by(username)

    elif user_choice == "6":
        edit = input("Please Enter The New Value: ")
        temp.set_mobile(edit)
        temp.set_update_date(date.today())
        temp.set_modified_by(username)

    # Category requires extra steps
    elif user_choice == "7":
        choice = input("""Please Enter The New Value:
     1) Development
     2) Office Fitting
     3) Support
     >>""")

        if choice == "1":
            edit = "Development"
        elif choice == "2":
            edit = "Office Fitting"
        elif choice == "3":
            edit = "Support"
        else:
            print("Incorrect Entry!")
            time.sleep(2)
            option6()

        temp.set_category(edit)
        temp.set_modified_by(username)

    # Decided to not allow user to edit creation date for data itegrity
    # elif user_choice == "8":
    #     edit = input("Please Enter The New Value: ")
    #     temp.set_creation_date(edit)
    #     temp.set_modified_by(username)

    # Decided to not allow user to edit modified date for data itegrity
    # elif user_choice == "9":
    #     edit = input("Please Enter The New Value: ")
    #     temp.set_update_date(edit)
    #     temp.set_modified_by(username)

    # Invalid input and 0 - Returns to Main Menu
    else:
        print("Invalid Input!")


def option4():
    """
    Function to remove a record, record selected via ID and confirmation required from user before deletion occurs
    :return:
    """
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
    answer = input("Is this the User you wish to Remove? Type Y/N").lower()

    if answer == "y":
        # Removing selected record from contact_list
        contact_list.remove(temp)
    else:
        print("Please Choose another ID - Use the search function to find ID choice")


def option5():
    """
    Function to contain the required reports
    :return:
    """
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


def option6():
    """
    Function which exits program, with option to save work to csv
    :return:
    """
    userinput = input("""***Exit Selected***
    Would you like to save your work? Y/N""").lower()

    if userinput == "y":
        write_data()
        print("Saved Successfully!")
        time.sleep(2)
        quit()
    else:
        print("Exit - Unsaved")
        time.sleep(2)
        quit()


def load_data():
    """
    Function to load csv file into list containing instances of Contact class
    :return:
    """
    # using CSVService read_data method to read in contacts.csv
    # Returns message to User if no file exists already
    # try:
    instance.read_data()
    # except IOError:
    #     print("File 'contacts.csv' Doesnt Exist!\n Continue and file called contacts.csv will be created!")
    #     time.sleep(2)
    # return 0

    # sends list containing header to Contact object, appending to first position in contact_list
    contact_list.append(Contact(instance.header))

    # Loops through lists contained within instance.data, adding each entry as a Contact object after header in contact_list
    for data in instance.data:
        contact_list.append(Contact(data))


def write_data():
    """
    Function to write the contents of the contact_list to csv file.
    :return:
    """

    #Loops through each contact in contact_list, appends full_details to write_list
    for contact in contact_list:
        write_list.append(contact.get_full_detail())


    instance.write_data(write_list)


def clear_screen():
    """
    Function to clear screen and improve UX
    :return:
    """
    print("\n\n\n\n\n\n\n\n\n\n\n\n")


def id_tracker():
    """
    Function to scan for highest ID number in contact_list in order to assign new ID's
    :return:
    """
    highest_id = 0

    # iterates over list, skipping first line (header)
    for contact in contact_list[1:]:
        temp = int(contact.get_id())
        if temp > highest_id:
            highest_id = temp

    # returns highest ID value in CSV, and add's one for the next ID
    return highest_id + 1


# Main Code
while True:
    # prompting user for username
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

        # runs id_tracker function, assigns return to variable
        current_id = id_tracker()

        while True:
            # calls on menu function
            menu()

            userinput = input(">")

            if userinput == "1":
                print("'Add a Contact' Selected")
                time.sleep(2)
                clear_screen()
                option1(current_id)

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
