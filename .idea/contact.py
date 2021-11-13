class Contact:

    # initialise Student Class, takes in a list, assigning the required elements to corresponding attributes
    def __init__(self, new_contact=[]):
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

    # Setters
    def set_id(self, new_id):
        self.id = new_id

    def set_fname(self, new_fname):
        self.fname = new_fname

    def set_lname(self, new_lname):
        self.lname = new_lname

    def set_company(self, new_company):
        self.company = new_company

    def set_address(self, new_address):
        self.address = new_address

    def set_landline(self, new_landline):
        self.landline = new_landline

    def set_mobile(self, new_mobile):
        self.mobile = new_mobile

    def set_category(self, new_category):
        self.category = new_category

    def set_creation_date(self, new_creation_date):
        self.creation_date = new_creation_date

    def set_update_date(self, new_update_date):
        self.update_date = new_update_date

    def set_modified_by(self, new_modified_by):
        self.modified_by = new_modified_by

    # Getters
    def get_id(self):
        return self.id

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_company(self):
        return self.company

    def get_address(self):
        return self.address

    def get_landline(self):
        return self.landline

    def get_mobile(self):
        return self.mobile

    def get_category(self):
        return self.category

    def get_creation_date(self):
        return self.creation_date

    def get_update_date(self):
        return self.update_date

    def get_modified_by(self):
        return self.modified_by

    def get_full_detail(self):
        return [self.id, self.fname, self.lname, self.company, self.address, self.landline,
                self.mobile, self.category, self.creation_date, self.update_date, self.modified_by]
