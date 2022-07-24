from random import randint
from threading import Thread
from time import time, sleep
import numpy as np
import argparser
import ping

args = argparser.parse()

a_min, a_max = 1, 223
b_min, b_max = 1, 254
c_min, c_max = 1, 254
d_min, d_max = 1, 254


def next_ip_random():
    while True:
        yield randint(a_min, a_max), randint(b_min, b_max),\
              randint(c_min, c_max), randint(d_min, d_max)


def next_ip_sequential():
    while True:
        for ip_d in range(d_min, d_max):
            for ip_c in range(c_min, c_max):
                for ip_b in range(b_min, b_max):
                    for ip_a in range(a_min, a_max):
                        yield ip_a, ip_b, ip_c, ip_d


THREAD_NUMBER = args.threads
threads = [None] * THREAD_NUMBER
results = [None] * THREAD_NUMBER
th_args = [None] * THREAD_NUMBER

ping_timeout, ping_count, ping_interval = args.timeout, args.count, args.interval

ip_gen = next_ip_random()

data = np.load('map.npy')

count = 0
count_pos = 0
count_neg = 0
t_init = time()
t0 = t_init
while True:
    # save every 10 minutes
    t1 = time()
    if t1 - t0 > 600:
        t0 = time()
        print(f'{str(int(t1 - t_init)).zfill(6)} {str(count).zfill(10)} '
              f'(+{round(count_pos/count, 2)} -{round(count_neg/count, 2)})')
        np.save('map.npy', data)

    # new ping
    for i in range(THREAD_NUMBER):
        # create thread
        if threads[i] is None:
            a, b, c, d = next(ip_gen)
            th_args[i] = a, b, c, d
            threads[i] = Thread(target=ping.ping,
                                args=(f'{a}.{b}.{c}.{d}', results, i,
                                      ping_timeout, ping_count, ping_interval))
            threads[i].start()
            sleep(0.01)
        # close thread
        elif not threads[i].is_alive():
            threads[i].join()
            sleep(0.01)
            result = results[i]
            args = th_args[i]
            if result[0]:
                if data[args[0], args[1], args[2], args[3]] in [0, 255]:
                    data[args[0], args[1], args[2], args[3]] = result[1]
                else:
                    data[args[0], args[1], args[2], args[3]] =\
                        min(result[1], data[args[0], args[1], args[2], args[3]])
                count_pos += 1
            else:
                data[args[0], args[1], args[2], args[3]] = 0
                count_neg += 1
            threads[i] = None
            count += 1

    sleep(0.1)
