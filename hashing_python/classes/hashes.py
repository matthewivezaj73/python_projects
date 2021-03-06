import hashlib
class hashes:
    """ 
    Creating a class that will represent the action of applying a hash to a string.
    """
    def __init__(self,hash_name,hash_type,hash_len):
        """
        Creating a method to initialize the program and initializing the attributes of the __init__ method.
        """
        self.hash_name = hash_name
        self.hash_type = hash_type
        self.hash_len = hash_len
    def encrypt(self,your_phrase):
        """
        A method that will encrypt a string by algorithm selected.
        """
        #Asking the user for their choice of encoding.
        algorithm = input("Please enter the type of encoding you would like to encode your string in: ")
        #Asking the individual for their name.
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.algorithm(your_phrase.encode())
        # creating a generic constructor
        generic = hashlib.new('sha1')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")