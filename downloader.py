'''
Date: 10-08-2020
Author: Pandas ID
'''


from urllib.parse import unquote
import requests as req
import time,re,os


def download(url):
    CHUNK = 1024
    content = req.get(url)
    size = round(int(content.headers.get('Content-Length'))/CHUNK)
    print(f'\n    -* Ukuran Video: {size} KB')
    print('    -* Mulai Mendownload....')
    with open('a.mp4', 'wb') as a:
        for data in content.iter_content(chunk_size=CHUNK):
            a.write(data)
    print('    -* Selesai Mendownload....')

def parse_url(url):
    res = req.get(url).text
    if 'video_redirect' in res:
        url_video = re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"', res)
        return unquote(url_video.group(1)).replace(';', '&')
    else:
        exit('    -! Video Tidak Ditemukan')

if __name__ == '__main__':
    os.system('clear')
    print('''
    █▀█ ▄▀█ █▄ █ █▀▄ ▄▀█ █▀
    █▀▀ █▀█ █ ▀█ █▄▀ █▀█ ▄█
    -----------------------
     [FB Video Downloader]
    -----------------------''')
    url = parse_url(input('\n    Url Video: ').replace('www', 'mbasic'))
    download(url)
    print('\n    -* Terima Kasih Sudah Menggunakan Tools Kami')
    print('    -* Silahkan Kunjungi: https://pandasid.blogspot.com Untuk Melihat Tools Kami Yang Lainnya:)')
