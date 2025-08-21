import time
import psutil
import numpy as np
import matplotlib.pyplot as plt
import os

def iterative_sum(arr):
    s = 0
    for i in range(len(arr)):
        s += int(arr[i])
    return s

def measure_for_ns(ns):
    times = []
    mems = []
    proc = psutil.Process(os.getpid())
    for n in ns:
        arr = np.arange(n, dtype=np.int64)

        t0 = time.perf_counter()
        _ = iterative_sum(arr)
        t1 = time.perf_counter()

        rss_mb = proc.memory_info().rss / (1024*1024)

        elapsed = t1 - t0
        print(f"n={n}  Tiempo = {elapsed:.6f} s")
        print(f"n={n}  Memoria = {rss_mb:.6f} MB")

        times.append(elapsed)
        mems.append(rss_mb)
    return times, mems

def main():
    ns = [100 * (10**i) for i in range(0,6)]  
    times, mems = measure_for_ns(ns)

    plt.figure(figsize=(8,5))
    plt.plot(ns, times, marker='o')
    plt.xscale('log')
    plt.xlabel('Datos (n)')
    plt.ylabel('Tiempo (s)')
    plt.title('Datos vs Tiempo - Interprete Iterativo')
    plt.grid(True)
    plt.savefig('interprete_iterative_time.png')
    plt.show()

    plt.figure(figsize=(8,5))
    plt.plot(ns, mems, marker='o')
    plt.xscale('log')
    plt.xlabel('Datos (n)')
    plt.ylabel('Memoria (MB)')
    plt.title('Datos vs Memoria - Interprete Iterativo')
    plt.grid(True)
    plt.savefig('interprete_iterative_memory.png')
    plt.show()

if __name__ == "__main__":
    main()
