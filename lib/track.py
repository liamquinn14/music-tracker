import emoji

def contains_emoji(text):
    for character in text:
        if character in emoji.EMOJI_DATA:
            return True
    return False

class Track():
    
    def __init__(self, artist, song_title):
        if artist == "":
            raise Exception("Artist field empty. Please provide a valid artist name.")
        elif song_title == "":
            raise Exception("Track title field empty. Please provide a valid track title.")
        elif contains_emoji(artist):
            raise Exception("Track artist contains an emoji. Please provide a valid artist name.")
        elif contains_emoji(song_title):
            raise Exception("Track title contains an emoji. Please provide a valid track title.")
        elif len(artist) > 140:
            raise Exception("Artist name is too long. Please provide an artist name containing no more than 140 characters.")
        elif len(song_title) > 140:
            raise Exception("Track title is too long. Please provide a track title containing no more than 140 characters.")
        self.artist = artist
        self.title = song_title
    
    def format_track_info(self):
        return f"{self.title} by {self.artist}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__