class Spending:
    """
    Created a class to represent
    """
    def __init__(self,account_name,account_remaining,account_life,account_increase,account_decrease,account_closure):
        """
        Initializing the following attributes:
            - account_name
            - account_remaining
            - account_life
            - account_increase
            - account_decrease
            - account_closure
        """            
        self.account_name = account_name
        self.account_remaining = account_remaining
        self.account_life = account_life
        self.account_increase = account_increase
        self.account_decrease = account_decrease
        self.account_closure = account_closure