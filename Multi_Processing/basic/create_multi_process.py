import multiprocessing
import time

def worker(name):
    print(f"Process {name} starting \n")
    time.sleep(2)
    print(f"Process {name} finished \n")



if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("P1",))
    p2 = multiprocessing.Process(target=worker, args=("P2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes finished")