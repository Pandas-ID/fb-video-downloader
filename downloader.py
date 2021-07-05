'''
Date: 10-08-2020
Author: Pandas ID
Last Update: 05-07-2021
'''


# import library
from urllib.parse import unquote
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import os


# kode warna
p = '\033[0m'
m = '\033[91m'
h = '\033[92m'
k = '\033[93m'


class Download:

    def __init__(self):
        pass

    def url(self, url):
        if re.search(r'www.facebook.com', url):
            url = url.replace('www', 'mbasic')

        # cek video
        try:
            response = requests.get(url).text
            self.video_url = re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"', response)

            if self.video_url is not None:
                # mendapatkan caption dari video
                meta = BeautifulSoup(response, 'html.parser').find('meta', {'property':'og:description'})
                try:
                    self.caption = meta['content']
                except:
                    self.caption = ''

                self.post_url  = url
                self.video_url = unquote(self.video_url.group(1))

                print(f'  (!) {h}Video ditemukan...{p}')
                self.download()
            else:
                print(f'  (!) {m}Video tidak ditemukan...{p}')
        except requests.exceptions.ConnectionError:
            print(f'   (!) {m}Koneksi error, mohon periksa koneksi internet Anda...{p}')
        except requests.exceptions.MissingSchema:
            print(f'  (!) {m}Url tidak valid...{p}')

    def info(self):
        print()
        print(f'  (•) {k}Caption:{p} {self.caption}')
        if self.video_size > 1024:
            self.video_size = round(self.video_size / 1024)
            m = 'mb'
        else:
            self.video_size = round(self.video_size)
            m = 'kb'
        print(f'  (•) {k}Ukuran video:{p} {self.video_size} {m}')
        print()


    def download(self):
        content = requests.get(self.video_url)
        self.video_size = int(content.headers.get('Content-Length'))/1024
        video_name = self.video_name
        try:
            with open('/sdcard/videos/'+video_name, 'wb') as fl:
                self.info()
                print(f'  (!) {h}Mulai mengunduh...{p}')
                fl.write(content.content)
            print(f'  (•) {k}Video tersimpan di {h}/sdcard/videos/{video_name}{p}')
            print(f'\n\n  Kontak:{h} https://t.me/PandasID\n{p}  Blog: {h}https://pandasid.blogspot.com\n')
        except FileNotFoundError:
            os.system('mkdir -p /sdcard/videos')
            self.download()

    @property
    def video_name(self):
        return datetime.now().strftime('%m%d%Y%-H%M%S')+'.mp4'

if __name__ == '__main__':
    os.system('clear')
    print(f'{h}█▀█ ▄▀█ █▄ █ █▀▄ ▄▀█ █▀'.center(72))
    print(f'█▀▀ █▀█ █ ▀█ █▄▀ █▀█ ▄█{p}'.center(72))
    print('-----------------------'.center(68))
    print(f'{h}[{p}FB Video Downloader{h}]{p}'.center(86))
    print('-----------------------'.center(68))
    print()

    download = Download()

    url = input(f'  (?) {k}url video: {p}')
    download.url(url)
