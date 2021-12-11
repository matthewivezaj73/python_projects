class Validate:
    """
    Creating a class to represent data validation
    """
    def __init__(self,Skey,Svalue):
        """
        Initializing the following attributes: 
        - Skey  
        - Svalue.
        """
        self.Skey = Skey
        self.Svalue = Svalue
    def validate_Key(self,key):
        """
        A method that is used to validate a key.
        """
        key_list = ["IPSec", "SSL", "TLS", "kerberos", "SSH", "SMTP", "HTTP", "HTTPS", "SFTP", "OSPF", "PCT", "ZRTP"]
        if key in key_list:
            return True
        else:
            return False
    def validate_Value(self,value):
        """
        A method that is used to validate a value.
        """
        if value.isdigit():
            return True
        else:
            return False