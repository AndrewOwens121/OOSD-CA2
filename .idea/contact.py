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

    def set_id(self,new_id):
        self.id = new_id
    def set_fname(self,new_fname):
        self.fname = new_fname
    def set_lname(self,new_lname):
        self.lname = new_lname
    def set_company(self):
        self.company = new_company
    def set_address(self):
        self.address = new_address
    def set_landline(self):
        self.landline = new_landlin
    def set_mobile(self):
        self.mobile = new_mobile
    def set_category(self):
        self.category = new_category
    def set_creation_date(self):
        self.creation_date = new_creation_date
    def set_update_date(self):
        self.update_date = new_update_date
    def set_modified_by(self):
        self.modified_by = new_modified_by





