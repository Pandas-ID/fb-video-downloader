'''
Date: 10-08-2020
Author: Pandas ID

Saya sengaja untuk tidak mengencode program yang saya buat,saya ingin
program ini dipelajari bagi mereka yang mau belajar bukan untuk mereka yang
cuma tau recode!!

Kalaupun Kalian mau meng upload program ini ke github Anda tolong jangan lupa
cantumkan github aslinya (guthub saya).

Semoga bermanfaat...
'''


from urllib.parse import unquote
import requests as req
import time,re,os


def download(url, path):
    CHUNK = 1024
    content = req.get(url)
    size = round(int(content.headers.get('Content-Length'))/CHUNK)
    print(f'\n    -* Ukuran Video: {size} KB')
    print('    -* Mulai Mendownload....')
    with open(path, 'wb') as a:
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
    path = input('    Simpan Ke: ')
    if '.mp4' in path:
        download(url, path)
    else:
        print('\n    Contoh:\n    Simpan Ke: /sdcard/video/nama_video.mp4')
        exit()
    print('\n    -* Terima Kasih Sudah Menggunakan Tools Kami')
    print('    -* Silahkan Kunjungi: https://pandasid.blogspot.com Untuk Melihat Tools Kami Yang Lainnya:)')
