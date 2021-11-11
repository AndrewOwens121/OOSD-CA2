from csv_service import CSVService

password = "Secret"
filename = "contacts.csv"
contact_list = []

#creating an instance of the CSVService class and passing it the contacts.csv filename
instance = CSVService(filename)

#prompting user for password
usrpswrd=input("Please enter password >>")

if usrpswrd == password:
    print("Correct password")
    # using CSVService read_data method to read in contacts.csv
    instance.read_data()
    while True:
        print(len(instance.data))


else:
    print("Incorrect password: Access Denied")
