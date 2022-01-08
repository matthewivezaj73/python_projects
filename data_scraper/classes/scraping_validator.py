class ScrapingValidator:
    """
    A class that represents checks against 
    the data entered into the scraper.
    """
    def __init__(self,sitename,wordcount):
        """
        Initializing the following attributes:
            - sitename
            - wordcount 
        """
        self.sitename = sitename
        self.wordcount = wordcount
    def validateSite(self,sitename):
        """
        A method that will validate a site name before
        it can be used by the program.

        This method accepts the following parameter(s):
        - sitename
        """