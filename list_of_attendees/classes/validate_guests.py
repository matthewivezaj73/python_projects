class Guests:
    """
    A class that represents the act of validating, 
    checking in, and reminding guests of the party.
    """
    def __init__(self, guestname, guestage, guestphone, guesttype):
        self.guestname = guestname
        self.guestage = guestage
        self.guestphone = guestphone 
        self.guesttype = guesttype
    def validate_guest_age(self,age):
        """
        A method that validates the guest's age.
        """
        if (len(age) > 0) and age.isdigit():
            return True
        else:
            return False
    def validate_guest_name(self, name):
        """
        A method that validates the guest's name.
        """
        guest_list = ['Karen', "Joe", "Arnold", "William", "Samantha", "Sarah", "Tegan"]
        if (len(name) > 0) and name.isalpha():
            return True
        else: 
            return False
    def validate_guest_phone(self, phone):
        """
        A method that validates the guest's phone number.
        """
        if ((len(phone) == 10) and phone.isdigit()):
            return True
        else:
            return False
    def validate_guest_type(self,Gtype):
        """
        A method that validates the guest type
        """
        #Creating a list of a position a guest may have.
        guest_type_list = ["Guest", "Host", "Hostess", "Maid of honor", "Man of the hour"]
        if Gtype in guest_type_list:
            return True
        else:
            return False
