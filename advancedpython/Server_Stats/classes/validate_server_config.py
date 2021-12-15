import psutil
class Server:
    """
    A  class that will represent verifications of inputs on a server.
    """
    def __init__(self,server_name,server_type,server_mem,server_hertz):
        self.server_name = server_name
        self.server_type = server_type
        self.server_mem = server_mem
        self.server_hertz = server_hertz
    def get_ac(self):
        """
        A method that will tell you if the ac is plugged in or not.
        """
        # In[8]:
        get_ac_var = psutil.sensors_battery().power_plugged
        print(get_ac_var)
    def get_virtual_mem(self):
        """
        A method that will tell you how much virtual memory is on the server.
        """