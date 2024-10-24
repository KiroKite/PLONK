import random
import time
from collections import Counter
from multiprocessing import Pool, cpu_count

def worker(_):
    # Generate one sum of 1000 random choices
    return sum(random.choices([-1, 1], k=1000)) # Bug: Will only result in even results because k is even. EX: (−1)+1+(−1)+1=0 and 1+1+1+(−1)=2. So, to get odd results make k=999 :)

if __name__ == "__main__":
    starttime = time.time()

    # Use multiprocessing to parallelize the task
    with Pool(cpu_count()) as pool:
        results = pool.map(worker, range(10_000_000))  # Parallel sum generation

    # Use Counter to count frequencies efficiently
    counter = Counter(results)

    # Collect and print results at once
    output = "\n".join(f"{key} {value}" for key, value in counter.items())
    print(output)

    endtime = time.time()
    print(f"Execution time: {endtime - starttime:.6f} seconds") # FYI: My pc took 70.6 seconds to run this code.
