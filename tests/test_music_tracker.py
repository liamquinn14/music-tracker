from lib.music_tracker import MusicTracker
from lib.track import Track

def test_add_track():
    music_tracker = MusicTracker()
    new_track = Track("ABBA", "Waterloo")
    music_tracker.add_track(new_track)
    assert music_tracker.tracks == [new_track]

def test_list_tracks():
    music_tracker = MusicTracker()
    new_track1 = Track("ABBA", "Waterloo")
    new_track2 = Track("ABBA", "Song Two")
    music_tracker.add_track(new_track1)
    music_tracker.add_track(new_track2)
    assert music_tracker.list_tracks() == ["Waterloo", "Song Two"]

def test_unique_artists():
    music_tracker = MusicTracker()
    new_track1 = Track("ABBA", "Waterloo")
    new_track2 = Track("ABBA", "Song Two")
    music_tracker.add_track(new_track1)
    music_tracker.add_track(new_track2)
    assert music_tracker.unique_artists() == ["ABBA"]

def test_initialise():
    music_tracker = MusicTracker()
    assert music_tracker.tracks == []
