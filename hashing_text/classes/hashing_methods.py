#Importing a library.
import hashlib
class Hashing:
    """
    A class that acts as a virtual representation 
    of a compilation of different hashing methods.
    """
    def __init__(self,hashed_message, encryption_type, byte_size):
        """
        Initializing the following attributes:
            - hashed_message
            - encryption type
            - byte size
        """
        self.hashed_message = hashed_message
        self.encryption_type = encryption_type
        self.byte_size = byte_size
    def hash_sha256(self,hashed_message):
        """
        Hashing a message in sha256.
        """
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.sha256(hashed_message.encode())
        # creating a generic constructor
        generic = hashlib.new('sha256')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")