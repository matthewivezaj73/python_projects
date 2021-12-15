import psutil
class Server:
    """
    A  class that will represent verifications of inputs on a server.
    """
    def __init__(self,server_name,server_type,server_mem,server_hertz):
        self.server_name = server_name

    def get_ac(self):
        """
        A method that will tell you if the ac is plugged in or not.
        """
        # In[8]:
        get_ac = psutil.sensors_battery().power_plugged
        print(get_ac)