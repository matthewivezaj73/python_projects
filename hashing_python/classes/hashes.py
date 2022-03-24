import hashlib
class hashes:
    """ 
    Creating a class that will represent the action of applying a hash to a string.
    """
    def encrypt(self,algorithm):
        #Asking the user for their choice of encoding.
        user_choice = input("Please enter the type of encoding you would like to encode your string in: ")
        #Asking the individual for their name.
        your_phrase = input(b"Please enter your text here: ")
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.algorithm(your_phrase.encode())
        # creating a generic constructor
        generic = hashlib.new('sha1')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")