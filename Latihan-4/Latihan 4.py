class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)

class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist

playlist = Playlist()
song1 = Song("Lose Yourself", "Eminem")
song2 = Song("Someone Like You", "Adele")

playlist.add_song(song1)
playlist.add_song(song2)
media_player = MediaPlayer(playlist)
for song in media_player.playlist.songs:
    print(song.title, "by", song.artist)
