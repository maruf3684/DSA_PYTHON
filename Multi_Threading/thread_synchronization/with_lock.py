import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:  # acquire lock
            counter += 1  # atomic now

threads = [threading.Thread(target=safe_increment) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)