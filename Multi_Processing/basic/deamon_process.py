import multiprocessing
import time

def background_task():
    while True:
        print("Daemon process running...")
        time.sleep(1)



if __name__ == "__main__":
    p = multiprocessing.Process(target=background_task, daemon=True)
    p.start()

    print("Main program finished")