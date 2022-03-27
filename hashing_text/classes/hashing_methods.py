class Hashing:
    """
    A class that acts as a virtual representation 
    of a compilation of different hashing methods.
    """
    def __init__(self,hashed_message, encryption_type):
        """
        Initializing the following attributes:
            - hashed_message
            - encryption type
            - byte size
        """
        self.hashed_message = hashed_message