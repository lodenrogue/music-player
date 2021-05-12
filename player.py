import os
from pathlib import Path
import argparse
from itertools import islice, cycle

from playlist import Playlist
from download import Downloader

from pydub import AudioSegment
import simpleaudio

PLAYLIST_DIR = f'{Path.home()}/.music'
DOWNLOADS_DIR = f'{PLAYLIST_DIR}/downloads'


class Player:

    def __init__(self):
        if not os.path.isdir(PLAYLIST_DIR):
            print(f'No config found at {PLAYLIST_DIR}')
            exit(1)

        if not os.path.isdir(DOWNLOADS_DIR):
            os.mkdir(DOWNLOADS_DIR)

        self.downloader = Downloader(DOWNLOADS_DIR)
        self.audio = None


    def list_playlists(self):
        playlists = []

        for f in os.listdir(PLAYLIST_DIR):
            if f.endswith('.playlist'):
                playlists.append(f.replace('.playlist', ''))

        playlists.sort()
        return playlists


    def list_songs(self, playlist_name):
        playlist = Playlist(PLAYLIST_DIR, playlist_name)
        return playlist.songs


    def play(self, playlist_name, offset=0):
        simpleaudio.stop_all()

        playlist = Playlist(PLAYLIST_DIR, playlist_name)
        self.current_playlist = playlist

        songs = cycle(playlist.songs)

        for song in islice(songs, offset, None):
            if self.current_playlist is not playlist:
                break

            if not self._download_exists(song):
                print(f'Downloading {song}')
                self.downloader.download(song)

            print(f'Playing {song}')
            self._play_audio(song)


    def _download_exists(self, song):
        path = os.path.join(DOWNLOADS_DIR, song)
        return os.path.isfile(path)


    def _play_audio(self, file_name):
        path = os.path.join(DOWNLOADS_DIR, file_name)
        sound = AudioSegment.from_file(path)

        self.audio = simpleaudio.play_buffer(
            sound.raw_data,
            num_channels=sound.channels,
            bytes_per_sample=sound.sample_width,
            sample_rate=sound.frame_rate
        )

        self.audio.wait_done()


def get_args():
    parser = argparse.ArgumentParser()

    (parser.add_argument(
        "playlist",
        help="target playlist"))

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    # Player().play(args.playlist)
    print(Player().list_playlists())
