class MusicTracker():

    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def list_tracks(self):
        return self.tracks