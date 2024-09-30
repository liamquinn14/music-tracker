class MusicTracker():

    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def list_tracks(self):
        return [track.title for track in self.tracks]
    
    def unique_artists(self):
        all_artists = [track.artist for track in self.tracks]
        return list(set(all_artists))