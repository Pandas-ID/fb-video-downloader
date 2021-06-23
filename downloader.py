'''
Date: 10-08-2020
Author: Pandas ID
'''



from urllib.parse import unquote
from bs4 import BeautifulSoup
from datetime import datetime
import requests as req
import re,os,time


p = '\033[0m'
m = '\033[91m'
h = '\033[92m'
k = '\033[93m'

class Downloader:

    __chunk = 1024

    def __init__(self):
        self.__url = ''
        self.__caption = ''
        self.__video_size = ''
        self.__video_name = datetime.now().strftime('%m%d%Y%-H%M%S')+'_pandas.mp4'

    def banner(self):
        os.system('clear')
        print(f'{h}█▀█ ▄▀█ █▄ █ █▀▄ ▄▀█ █▀'.center(72))
        print(f'█▀▀ █▀█ █ ▀█ █▄▀ █▀█ ▄█{p}'.center(72))
        print('-----------------------'.center(68))
        print(f'{h}[{p}FB Video Downloader{h}]{p}'.center(86))
        print('-----------------------'.center(68))
        print()

    # meminta inputan url dari user
    def setUrl(self):
        url = input(f'  >{k} url: {p}');print(p)
        self.__url = url.replace('www', 'mbasic')

    # mengecek url yang dimasukan user jika benar akan mengembalikan url yang telah di parse
    def cekUrl(self):
        response = req.get(self.__url).text
        if 'video_redirect' in response:
            print(f'  >{h} video found!')
            self.getVideoInfo()
            url_video = re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"', response)
            self.__url = unquote(url_video.group(1)).replace(';', '&')
        else:
            exit(f'  >{m} video not found!')

    def getVideoInfo(self):
        response = req.get(self.__url)

        # mendapatkan caption dari video
        meta = BeautifulSoup(response.text, 'html.parser').find('meta', {'name':'description'})
        try:
            self.__caption= meta['content']
        except:
            pass

    def showVideoInfo(self):
        print(f'\n{p}  > {k}caption:{p} {self.__caption}\n{p}  >{k} video size:{p} {self.__video_size} KB')

    def download(self):
        content = req.get(self.__url)
        # mendapatkan ukuran video
        size = round(int(content.headers.get('Content-Length'))/self.__chunk)
        self.__video_size = size
        self.showVideoInfo()
        print(f'\n{p}  >{h} Is downloading...', end='', flush=True)
        with open('/sdcard/'+self.__video_name, 'wb') as vid:
            for data in content.iter_content(chunk_size=self.__chunk):
                vid.write(data)
        print(f'\n{p}  >{k} videos saved on directory{h} /sdcard/{self.__video_name}')

    def about(self):
        print(f'\n\n{p}  > My Contact:\n{h}    https://t.me/PandasID\n{p}  > My Blog:\n{h}    https://pandasid.blogspot.com\n\n')

if __name__ == '__main__':
    # memuat objek dari class "Downloader"
    downloader = Downloader()

    downloader.banner()
    downloader.setUrl()
    downloader.cekUrl()
    downloader.download()
    downloader.about()
