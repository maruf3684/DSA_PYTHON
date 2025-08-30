# 4. CPU Core Utilization & Affinity
# 	•	Each process runs independently on a CPU core.
# 	•	By default, OS schedules processes automatically across cores.
# 	•	Affinity allows you to bind a process to specific cores (Linux/Windows support differs).

import multiprocessing
import os
import psutil
import time

def task(name):
    print(f"{name} PID: {os.getpid()}")
    p = psutil.Process(os.getpid())
    print(f"{name} affinity: {p.cpu_affinity() if hasattr(p, 'cpu_affinity') else 'Not supported'}")
    time.sleep(2)


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=task, args=(f"P{i}",)) for i in range(2)]

    for p in processes: p.start()
    for p in processes: p.join()