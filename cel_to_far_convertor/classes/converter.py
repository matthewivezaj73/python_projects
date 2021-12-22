class converter:
    """
    A class that converts different values.
    """
    def __init__(self,temperature):
        """
        Initializing attributes.
        """
        self.temperature = temperature
    def celsius_fahrenheit_converter(self,celsius):
        """
        Takes in a value in celsius and converts it into fahrenheit.
        """
        try:
            if ("." in celsius) and (celsius.replace('.','')).isdigit() or celsius.isdigit():
                print(float(celsius) * 9 / 5 + 32)
                return True
            else:
                print(f"\'{celsius}\' is not a numerical value!")
                return False
        except TypeError:
            print(f"Sorry, but it appears \'{celsius}\' is an improper data type.")
    def celsius_kelvin_converter(self,celsius):
        """
        Takes in a value in celsius and converts it into kelvin.
        """
        return 273.15 + celsius