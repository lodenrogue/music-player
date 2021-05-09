import os


class Playlist:

    def __init__(self, playlist_dir, playlist_name):
        path = os.path.join(playlist_dir, f'{playlist_name}.playlist')

        if not os.path.isfile(path):
            print(f'No playlist found in {path}')
            exit(1)

        with open(path) as f:
            self.songs = [song.strip() for song in f]
