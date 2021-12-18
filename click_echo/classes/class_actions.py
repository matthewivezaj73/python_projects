class Metrics:
    def __init__(self,metric_name,metric_value,quantity_of_metrics):
        """
        Initializing the following attributes.
            - metric_name
            - metric_value
            - quantity_of_metrics
        """
        self.metric_name = metric_name
        self.metric_value = metric_value
        self.quantity_of_metrics = quantity_of_metrics
    def ac_connected():
        """
        A function that checks to see if the power is connected 
        to the system. If it is, the function will return true.
        """
        ac_power = psutil.sensors_battery().power_plugged
        if ac_power is True:
            print("The ac adapter is connected.")
        else:
            print("The ac adapter is not connected.")
    def command_line(argv):
        """
        A function that runs other user 
        defined functions inside of it.
        """
        #Try block
        try:
            program_name, *arguments = argv
            if not arguments:
                show_sensors()
            elif arguments and arguments[0] == '--help':
                print(HELP_TEXT.format(program_name=program_name))
                return
        except ValueError:
            print("Unknown arguments {}".format(arguments))
    def cpu_load():
        """
        A function that checks the total amount of ram available 
        on the system and displays it within intercals of a tenth of a percent.
        """
        cpu_interval = psutil.cpu_percent(interval=0.1)
        print(cpu_interval)
    def ip_addresses():
        """
        A function the gets the hostname, IP address 
        information, and appends everything to a list.
        """
        hostname = socket.gethostname()
        addresses = socket.getaddrinfo(socket.gethostname(), None)
        address_info = []
        for address in addresses:
            address_info.append((address[0].name, address[4][0]))
        return address_info
    def python_version():
        """
        A function that checks the version of python you are running.
        """
        return sys.version_info
    def ram_available():
        """
        A function that shows the user the 
        total amount of memory available on a system.
        """
        return psutil.virtual_memory().available
    def show_arg(argv):
        parser = argparse.ArgumentParser(
            description='Displays the values of the sensors',
            add_help=True,
        )
        arguments = parser.parse_args()
        show_sensors()
    def show_sensors():
        """
        A function the displays the following:
            - cpu internval
            - Ram available
            - ac connection status
            - IP addresses
        """
        print("Python version: {0.major}.{0.minor}".format(python_version()))
        for address in ip_addresses():
            print(f"IP addresses: {address})")
        print(f"CPU Load: {cpu_load()}")
        print("RAM Available: {} MiB".format(ram_available() / 1024**2))