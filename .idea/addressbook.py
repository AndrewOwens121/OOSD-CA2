class Addressbook:
    def __init__(self, addressbookname):
        self.addressbookname = addressbookname
        self.contact_list = []

    # Search methods below - All return a list of the search matches

    def id_search(self, search_id):
        search_result = []

        for contact in self.contact_list:
            if contact.id == search_id:
                search_result.append(contact.get_full_detail())

        return search_result

    def fname_search(self, search_fname):
        search_result = []

        for contact in self.contact_list:
            if contact.fname == search_fname:
                search_result.append(contact.get_full_detail())

        return search_result

    def lname_search(self, search_lname):
        search_result = []

        for contact in self.contact_list:
            if contact.lname == search_lname:
                search_result.append(contact.get_full_detail())

        return search_result

    def company_search(self, search_company):
        search_result = []

        for contact in self.contact_list:
            if contact.company == search_company:
                search_result.append(contact.get_full_detail())

        return search_result

    def address_search(self, search_address):
        search_result = []

        for contact in self.contact_list:
            if contact.address == search_address:
                search_result.append(contact.get_full_detail())

        return search_result

    def landline_search(self, search_landline):
        search_result = []

        for contact in self.contact_list:
            if contact.landline == search_landline:
                search_result.append(contact.get_full_detail())

        return search_result

    def mobile_search(self, search_mobile):
        search_result = []

        for contact in self.contact_list:
            if contact.mobile == search_mobile:
                search_result.append(contact.get_full_detail())

        return search_result

    def category_search(self, search_category):
        search_result = []

        for contact in self.contact_list:
            if contact.category == search_category:
                search_result.append(contact.get_full_detail())

        return search_result

    def creation_date_search(self, search_creation_date):
        search_result = []

        for contact in self.contact_list:
            if contact.creation_date == search_creation_date:
                search_result.append(contact.get_full_detail())

        return search_result

    def update_date_search(self, search_update_date):
        search_result = []

        for contact in self.contact_list:
            if contact.update_date == search_update_date:
                search_result.append(contact.get_full_detail())

        return search_result

    def modified_by_search(self, search_modified_by):
        search_result = []

        for contact in self.contact_list:
            if contact.modified_by == search_modified_by:
                search_result.append(contact.get_full_detail())

        return search_result

    def edit_search(self, search_id):
        for contact in self.contact_list:
            if contact.get_id() == search_id:
                return contact

    def full_contact_list(self):
        return self.contact_list

    def development_list(self):
        search_result = []

        for contact in self.contact_list:
            if contact.get_category() == "Development":
                search_result.append(contact)

        return search_result

    def support_list(self):
        search_result = []

        for contact in self.contact_list:
            if contact.get_category() == "Support":
                search_result.append(contact)

        return search_result

    def office_fitting_list(self):
        search_result = []

        for contact in self.contact_list:
            if contact.get_category() == "Office Fitting":
                search_result.append(contact)

        return search_result

    #method to grab highest ID in the csv, for assigning future ID's
    def highest_id(self):
        highest_id = 0
        for contact in self.contact_list[1:]:
            temp = int(contact.get_id())
            if temp > highest_id:
                highest_id = temp
        return highest_id


