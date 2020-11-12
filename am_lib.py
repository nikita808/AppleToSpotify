from libpytunes import Library

class Song:
    def __init__(self, artist, name):
        self.Artist = artist
        self.Name = name


SongList = []

l = Library("C:/Users/Admin/Desktop/Library.xml")

for id, song in l.songs.items():
    SongList.append(Song(song.artist, song.name))