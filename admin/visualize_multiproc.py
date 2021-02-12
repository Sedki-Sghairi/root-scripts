#!/usr/bin/env python3
import time
import concurrent.futures

start= time.perf_counter()


def do_something(sec):
    print(f'Sleeping {sec} sec..')
    time.sleep(sec)
    return f'Done sleeping in {sec}'

with concurrent.futures.ProcessPoolExecutor() as executor:
     secs = [5,4,3,2,1]
     results  = executor.map(do_something,secs)
     for res in results:
         print(res)

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')
