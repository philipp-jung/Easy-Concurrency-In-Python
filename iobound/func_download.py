# func_download.py
import urllib.request
import time


def download_img(pic_id, url):
    res = urllib.request.urlopen(url)
    pic = res.read()
    with open(f'./{pic_id}.jpg', 'wb') as f:
        f.write(pic)
    print(f'Picture {pic_id} saved!')


def main():
    args = [(n, f'https://picsum.photos/id/{n}/200/300') for n in range(20)]
    start = time.time()
    for pic_id, url in args:
        download_img(pic_id, url)
    end = time.time()
    print('Operation took {:.3f} seconds to complete.'.format(end-start))


if __name__ == '__main__':
    main()
