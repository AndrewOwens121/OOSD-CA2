class Contacts:
    #initialise Student Class, assigning the required parameters to attributes as per below
    def __init__(self,new_contact=[]): #new_id,new_fname,new_lname,new_company, new_address,new_landline,new_mobile, new_category, new_creation_date, new_update_date, new_modified_by):
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
        # self.id = new_id
        # self.fname = new_fname
        # self.lname = new_lname
        # self.company = new_company
        # self.address = new_address
        # self.landline = new_landline
        # self.mobile = new_mobile
        # self.category = new_category
        # self.creation_date = new_creation_date
        # self.update_date = new_update_date
        # self.modified_by = new_modified_by
