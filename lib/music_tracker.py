class MusicTracker():

    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        if track in self.tracks:
            raise Exception("Track already in library. If you wish to add a duplicate track, use the 'add_duplicate_track' method.")
        else:
            self.tracks.append(track)
    
    def add_duplicate_track(self, track):
        if track not in self.tracks:
            raise Exception("Attempted to add non-duplicate track as a duplicate. Use 'add_track' method instead.")
        else:
            self.tracks.append(track)

    def list_tracks(self):
        return [track.format_track_info() for track in self.tracks]
    
    def unique_artists(self):
        all_artists = [track.artist for track in self.tracks]
        return list(set(all_artists))
    