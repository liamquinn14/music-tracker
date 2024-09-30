from lib.track import Track

def test_artist():
    new_track = Track("ABBA", "Waterloo")
    assert new_track.artist == "ABBA"

def test_title():
    new_track = Track("ABBA", "Waterloo")
    assert new_track.title == "Waterloo"
    