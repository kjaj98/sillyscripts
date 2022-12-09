import concurrent.futures
import numpy as np
import time
import check_pair_distances as func



if __name__ =='__main__':
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        labels = np.arange(10)
        results = executor.map(func.do_stuff, labels)
    finish = time.perf_counter()
    print(f'Finished in parallel calc in {round(finish-start, 2)} second(s)')
    
