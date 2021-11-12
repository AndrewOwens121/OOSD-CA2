class Contact:

    #initialise Student Class, takes in a list, assigning the required elements to corresponding attributes
    def __init__(self,new_contact=[]):
        self.id = new_contact[0]
        self.fname = new_contact[1]
        self.lname = new_contact[2]
        self.company = new_contact[3]
        self.address = new_contact[4]
        self.landline = new_contact[5]
        self.mobile = new_contact[6]
        self.category = new_contact[7]
        self.creation_date = new_contact[8]
        self.update_date = new_contact[9]
        self.modified_by = new_contact[10]




