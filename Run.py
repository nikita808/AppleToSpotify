import os

import am_lib

from transfer_tool import SpotifyClient

spotify_token = input('Please enter your Spotify Token: ')
spotify_client = SpotifyClient(spotify_token)



def run():
    for song in am_lib.SongList:
        spotify_song_id = spotify_client.searchSong(song.Artist, song.Name)
        if spotify_song_id:
            added_song = spotify_client.add_song(spotify_song_id)
            if added_song:
                print(f'Added {song.Artist} - {song.Name}')

run()