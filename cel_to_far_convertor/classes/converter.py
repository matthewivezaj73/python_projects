class converter:
    """
    A class that converts different values.
    """
    def __init__(self,temperature):
        """
        Initializing attributes.
        """
        self.temperature = temperature
    def celcius_fahrenheit_converter(self,celsius):
        """
        Takes in a value in celsius and converts it into fahrenheit.
        """
        if ("." in celsius) and (celsius.replace('.','')).isdigit() or celsius.isdigit():
            return celsius * 9 / 5 + 32
    def celcius_kelvin_converter(self,celsius):
        """
        Takes in a value in celsius and converts it into kelvin.
        """
        return 273.15 + celsius