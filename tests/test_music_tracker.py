from lib.music_tracker import *

# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

def test_add_track():
    music_tracker = MusicTracker()
    music_tracker.add_track("Waterloo by ABBA")
    assert music_tracker.tracks == ["Waterloo by ABBA"]

def test_list_tracks():
    music_tracker = MusicTracker()
    music_tracker.add_track("Waterloo by ABBA")
    music_tracker.add_track("Song1 by ABBA")
    assert music_tracker.list_tracks() == ["Waterloo by ABBA", "Song1 by ABBA"]

def test_initialise():
    music_tracker = MusicTracker()
    assert music_tracker.tracks == []
