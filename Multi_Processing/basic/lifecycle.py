# 3. Process Lifecycle: start, join, terminate
# 	•	start() → start the process
# 	•	join(timeout) → wait for process to finish
# 	•	terminate() → forcibly stop the process


import multiprocessing
import time

def task():
    for i in range(5):
        print(f"Running iteration {i}")
        time.sleep(1)


if __name__ == "__main__":
    p = multiprocessing.Process(target=task)
    print("Before start:", p.is_alive())

    p.start()
    print("After start:", p.is_alive())

    time.sleep(2)
    print("Terminating process...")
    p.terminate()  # forcibly stop
    p.join()
    print("After join:", p.is_alive())