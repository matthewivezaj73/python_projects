class ValidateMusic:
    """
    Created a class that represents a 
    validator for the music content entered.
    """
    def __init__(self,artist_name,album_name,song_title):
        """
        Creating a main method that initilzes the attributes.
        """
        self.artist_name = artist_name
        self.album_name = album_name
        self.song_title = song_title
    def __str__(self):
        """
        Listing the attrbutes from the main method.
        """
        return f'the musician {self.artist_name}\n\nthe Album name is {self.album_name}\n\nThe Song title is {self.song_title}'
    def play_song(self,song_name):
        """
        
        """