from youtube_dl import YoutubeDL


class Downloader:

    def __init__(self, download_dir):
        self.download_dir = download_dir

    def download(self, song):
        options = {
            'format': 'aac/mp3/ogg/wav/3gp/m4a/mp4',
            'outtmpl': f'{self.download_dir}/{song}',
            'quiet': 'True'
        }

        with YoutubeDL(options) as ytdl:
            ytdl.extract_info(f'ytsearch:{song} song', download=True)['entries'][0]
