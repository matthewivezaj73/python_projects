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
        return f'The musician is {self.artist_name}\n\nThe Album name is {self.album_name}\n\nThe Song title is {self.song_title}'
    def play_song(self,artist_name,album_name,song_name):
        """
        Created a method that represents the act of playing a song.

        Takes the song name as parameters.
        """
        print(f'Now playing {song_name} by {artist_name} from the album {album_name}')
    def validate_album(self,album_name):
        """
        Creating a method that validates the album name.

        The method takes in album_name as a passed parameter.
        """
        if len(album_name) > 0:
            return True
        else:
            return False
    def validate_artist(self,artist_name):
        """
        Creating a method that validates the artist name.

        The method takes in artist_name as a passed parameter.
        """
        if (("'" in artist_name) and (artist_name.replace("'","").isalpha())) or artist_name.isalpha() or (("$" in artist_name) and (artist_name.replace("$","").isalpha())) or (("-" in artist_name) and (artist_name.replace("-","").isalpha())) or (("." in artist_name) and (artist_name.replace(".","").isalpha())):
            return True
        else:
            return False