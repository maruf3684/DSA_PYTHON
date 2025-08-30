import threading

rlock = threading.RLock()

def func_a():
    with rlock:
        func_b()

def func_b():
    with rlock:
        print("Inside func_b")

thread = threading.Thread(target=func_a)
thread.start()
thread.join()