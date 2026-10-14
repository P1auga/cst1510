import random

playlist = ["Song A", "Song B", "Song C", "Song D"]

def add_song(song):
    playlist.append(song)

def remove_song(song):
    if song in playlist:
        playlist.remove(song)

def shuffle():
    random.shuffle(playlist)
    print("Shuffled playlist:", playlist)

add_song("Song E")
remove_song("Song B")
print("Playlist:", playlist)
shuffle()
