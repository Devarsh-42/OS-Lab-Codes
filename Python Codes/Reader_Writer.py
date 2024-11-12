import threading
import time

read_count = 0
read_lock = threading.Semaphore(1)  
resource = threading.Semaphore(1)    

class Reader(threading.Thread):
    def run(self):
        global read_count

        try:
            read_lock.acquire()
            read_count += 1
            if read_count == 1:
                resource.acquire() 
            read_lock.release()

            print(f"{threading.current_thread().name} is reading.")
            time.sleep(1)  
            print(f"{threading.current_thread().name} has finished reading.")

            read_lock.acquire()
            read_count -= 1
            if read_count == 0:
                resource.release()  
            read_lock.release()

        except Exception as e:
            print(e)

class Writer(threading.Thread):
    def run(self):
        try:
            resource.acquire()

            print(f"{threading.current_thread().name} is writing.")
            time.sleep(1)  
            print(f"{threading.current_thread().name} has finished writing.")

            resource.release()

        except Exception as e:
            print(e)

reader1 = Reader()
reader2 = Reader()
writer1 = Writer()
writer2 = Writer()

reader1.start()
writer1.start()
reader2.start()
writer2.start()

reader1.join()
reader2.join()
writer1.join()
writer2.join()
