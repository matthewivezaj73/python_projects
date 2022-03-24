class hashes:
    """ 
    Creating a class that will represent the action of applying a hash to a string.
    """
    def encrypt(self,algorithm):
    
        #Asking the individual for their name.
        your_phrase = input(b"Please enter your text here: ")
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.sha1(your_phrase.encode())
        # creating a generic constructor
        generic = hashlib.new('sha1')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")