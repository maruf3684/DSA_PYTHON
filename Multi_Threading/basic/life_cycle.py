# 3. Thread Lifecycle
# 	1.	New → created but not started
# 	2.	Runnable → after start()
# 	3.	Running → executing run()
# 	4.	Terminated → finished execution
#
# Key methods:
# 	•	start() → start thread
# 	•	join(timeout) → wait for completion
# 	•	is_alive() → check if thread is running
# 	•	run() → method executed when thread starts


import threading
import time

def task():
    print("Running task")
    time.sleep(2)
    print("Task finished")

t = threading.Thread(target=task)
print("Is alive before start:", t.is_alive())

t.start()
print("Is alive after start:", t.is_alive())

t.join()
print("Is alive after join:", t.is_alive())