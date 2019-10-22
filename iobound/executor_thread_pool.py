# executor_thread_pool.py
import numpy as np
import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor


def download_img(pic_id, url):
    res = urllib.request.urlopen(url)
    pic = res.read()
    with open(f'./{pic_id}.jpg', 'wb') as f:
        f.write(pic)
    print(f'Picture {pic_id} saved!')


def main():
    times = []
    for _ in range(10):
        start = time.time()
        pic_ids = list(range(20))
        urls = [f'https://picsum.photos/id/{n}/200/300' for n in range(20)]
        with ThreadPoolExecutor(20) as executor:
            executor.map(download_img, pic_ids, urls)
        end = time.time()
        times.append(end-start)
    print('Operation took {:.3f} seconds on average to complete.'.format(np.mean(times)))


if __name__ == '__main__':
    main()
