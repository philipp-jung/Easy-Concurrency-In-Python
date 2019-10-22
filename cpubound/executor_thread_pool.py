# executor_thread_pool.py
import time
import numpy as np
from concurrent.futures import ThreadPoolExecutor


def fib(n):
    " returns n-th fibnonacci-number "
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    fib_range = list(range(1, 36))
    times = []
    for run in range(10):
        start = time.time()
        with ThreadPoolExecutor() as executor:
            executor.map(fib, fib_range)
        end = time.time()
        times.append(end-start)
        print('ended run ' + str(run) + ' in ' + str(times[run]) + 's')
    print('Computing fib up to fib(35) took {:.3f} seconds on average to complete.'.format(np.mean(times)))


if __name__ == '__main__':
    main()
