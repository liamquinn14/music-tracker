import pytest
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
    assert music_tracker.list_tracks() == ["Waterloo by ABBA", "Song Two by ABBA"]

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

# What if somebody wants to add the same track multiple times (i.e. they really love Waterloo)? (Whichever route you decide - have a test for it, so that the behaviour is explicit)

def test_unintentional_duplicate():
    music_tracker = MusicTracker()
    new_track1 = Track("ABBA", "Waterloo")
    music_tracker.add_track(new_track1)
    new_track2 = Track("ABBA", "Waterloo")
    with pytest.raises(Exception) as e:
        music_tracker.add_track(new_track2)
    error_message = str(e.value)
    assert error_message == "Track already in library. If you wish to add a duplicate track, use the 'add_duplicate_track' method."

def test_intentional_duplicate():
    music_tracker = MusicTracker()
    new_track1 = Track("ABBA", "Waterloo")
    music_tracker.add_track(new_track1)
    new_track2 = Track("ABBA", "Waterloo")
    music_tracker.add_duplicate_track(new_track2)
    assert music_tracker.list_tracks() == ["Waterloo by ABBA", "Waterloo by ABBA"]

def test_add_non_duplicate_as_duplicate():
    # Potentially unnecessary since it could be handled client side, only allowing the 'add_duplicate_track' method if the user tries to add a duplicate using the 'add_track' method
    music_tracker = MusicTracker()
    new_track1 = Track("ABBA", "Waterloo")
    with pytest.raises(Exception) as e:
        music_tracker.add_duplicate_track(new_track1)
    error_message = str(e.value)
    assert error_message == "Attempted to add non-duplicate track as a duplicate. Use 'add_track' method instead."

# It might be good to have a test which demonstrates the tracks are unique to a particular instance of the class, i.e. demonstrating that you haven't accidentally created global variables. (Create a tracker1, create a tracker2, add a track to each, and assert that each tracker only has its relevant track.)

def test_music_trackers_are_locally_scoped():
    music_tracker1 = MusicTracker()
    new_track1 = Track("ABBA", "Waterloo")
    music_tracker1.add_track(new_track1)
    music_tracker2 = MusicTracker()
    new_track2 = Track("Michael Jackson", "Thriller")
    music_tracker2.add_track(new_track2)
    assert music_tracker1.list_tracks() == ["Waterloo by ABBA"]
    assert music_tracker2.list_tracks() == ["Thriller by Michael Jackson"]