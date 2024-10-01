import pytest
from lib.track import Track

def test_artist():
    new_track = Track("ABBA", "Waterloo")
    assert new_track.artist == "ABBA"

def test_title():
    new_track = Track("ABBA", "Waterloo")
    assert new_track.title == "Waterloo"

def test_format_track_info():
    new_track = Track("ABBA", "Waterloo")
    assert new_track.format_track_info() == "Waterloo by ABBA"

# What if someone tries to add a blank track (empty string) - do you want to add an empty track to the tracker?

def test_empty_artist():
    with pytest.raises(Exception) as e:
        Track("", "Waterloo")
    error_message = str(e.value)
    assert error_message == "Artist field empty. Please provide a valid artist name."

def test_empty_title():
    with pytest.raises(Exception) as e:
        Track("ABBA", "")
    error_message = str(e.value)
    assert error_message == "Track title field empty. Please provide a valid track title."

# Think about other interesting edge cases when it comes to strings. Can you store/retrieve special characters? What about emoji?

# I've seen song titles with special characters in. But not an artist name? I'll assume for now that artist names with special characters are invalid but it's valid for song titles to contain special characters.

def test_special_character_in_artist():
    with pytest.raises(Exception) as e:
        Track("ABBA!!!", "Waterloo")
    error_message = str(e.value)
    assert error_message == "Artist name contains special characters. Please provide a valid artist name."

def test_special_character_in_title():
    new_track = Track("ABBA", "Waterloo!!!")
    assert new_track.format_track_info() == "Waterloo!!! by ABBA"

def test_emoji_in_artist():
    with pytest.raises(Exception) as e:
        Track("Emoji ABBA😊", "Waterloo")
    error_message = str(e.value)
    assert error_message == "Track artist contains an emoji. Please provide a valid artist name."

def test_emoji_in_title():
    with pytest.raises(Exception) as e:
        Track("ABBA", "Emoji Waterloo😊")
    error_message = str(e.value)
    assert error_message == "Track title contains an emoji. Please provide a valid track title."

# Do you think there should be an upper limit to the length of strings that you accept? If you say "no": does that mean it's okay if someone inputs a 1 million character string? If you say "no" to that: so what should the limit be? :)

# There are practical limits with extremely long track names. My research found that there have been instances where long track names (over 140 characters) caused crashes in iTunes. For now I'll assume that 140 characters is a reasonable limit for artist/track names.

def test_too_long_artist_names():
    long_artist_name = "Lorem ipsum dolor sit amet consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris lorem ipsum dolor sit amet"
    assert len(long_artist_name) > 140
    with pytest.raises(Exception) as e:
        new_track = Track(long_artist_name, "Waterloo")
        new_track.format_track_info()
    error_message = str(e.value)
    assert error_message == "Artist name is too long. Please provide an artist name containing no more than 140 characters."

def test_too_long_track_names():
    long_track_name = "Lorem ipsum dolor sit amet consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris lorem ipsum dolor sit amet"
    assert len(long_track_name) > 140
    with pytest.raises(Exception) as e:
        new_track = Track("ABBA", long_track_name)
        new_track.format_track_info()
    error_message = str(e.value)
    assert error_message == "Track title is too long. Please provide a track title containing no more than 140 characters."

