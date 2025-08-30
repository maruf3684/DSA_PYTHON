# 2. Daemon vs Non-Daemon Threads
# 	•	Daemon threads: Run in the background. Python will exit even if daemon threads are alive.
# 	•	Non-daemon threads: Main program waits until they finish.

import threading
import time

def background_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

t = threading.Thread(target=background_task, daemon=True)
t.start()

print("Main program finished")  # exits immediately