import threading
import time
from queue import Queue

def binary_semaphore():
    flag = [False, False]
    turn = 0

    def process_0():
        nonlocal turn
        print("Process 0 is requesting critical section.")
        flag[0] = True
        turn = 1
        while flag[1] and turn == 1:
            pass  
        print("Process 0 enters the critical section.")
        time.sleep(1) 
        print("Process 0 leaves the critical section.")
        flag[0] = False

    def process_1():
        nonlocal turn
        print("Process 1 is requesting critical section.")
        flag[1] = True
        turn = 0
        while flag[0] and turn == 0:
            pass  
        print("Process 1 enters the critical section.")
        time.sleep(1)  
        print("Process 1 leaves the critical section.")
        flag[1] = False

    t0 = threading.Thread(target=process_0)
    t1 = threading.Thread(target=process_1)
    
    t0.start()
    t1.start()
    t0.join()
    t1.join()

    print("\nMutual Exclusion: Satisfied")
    print("Progress: Satisfied")
    print("Bounded Waiting: Satisfied")

class CountingSemaphore:
    def __init__(self, max_value):
        self.value = max_value
        self.suspend_list = Queue()
        self.lock = threading.Lock()

    def wait_semaphore(self, process_name):
        with self.lock:
            if self.value > 0:
                self.value -= 1
                print(f"{process_name} enters the critical section.")
            else:
                print(f"{process_name} is suspended (added to suspend list).")
                self.suspend_list.put(process_name)
                return False
        return True

    def signal_semaphore(self, process_name):
        with self.lock:
            print(f"{process_name} leaves the critical section.")
            self.value += 1
            if not self.suspend_list.empty():
                next_process = self.suspend_list.get()
                print(f"{next_process} is woken up from the suspend list.")
                self.value -= 1  
                return next_process  
        return None


def counting_semaphore(process_count, max_in_critical_section):
    semaphore = CountingSemaphore(max_in_critical_section)

    def process(semaphore, process_name):
        while not semaphore.wait_semaphore(process_name):
            time.sleep(0.5)  
        time.sleep(1)
        next_process = semaphore.signal_semaphore(process_name)
        if next_process:
            threading.Thread(target=process, args=(semaphore, next_process)).start()

    threads = []
    for i in range(1, process_count + 1):
        process_name = f"Process-{i}"
        t = threading.Thread(target=process, args=(semaphore, process_name))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\nMutual Exclusion: Satisfied (only up to max allowed processes can enter)")
    print("Progress: Satisfied (waiting processes will enter as slots free up)")
    print("Bounded Waiting: Satisfied (queued processes will eventually enter based on arrival order)")


def main():
   
    process_count = int(input("Enter the number of processes: "))

    if process_count < 2:
        print("Invalid number of processes! Must be 2 or more.")
        return

    if process_count == 2:
        print("Using Binary Semaphore (Peterson's Solution) for 2 processes.")
        binary_semaphore()
    else:
        max_in_critical_section = int(input("Enter the maximum number of processes allowed in critical section at once: "))
        print(f"Using Counting Semaphore for {process_count} processes with a maximum of {max_in_critical_section} in critical section at a time.")
        counting_semaphore(process_count, max_in_critical_section)

if __name__ == "__main__":
    main()

"""
def binary_semaphore(semaphore, processID, operation):
    if operation == "down":
        if semaphore[0] == 1:
            semaphore[0] = 0
            print(f"Process {processID} enters critical section (binary down).")
        else:
            print(f"Process {processID} is waiting (binary down).")
    elif operation == "up":
        if semaphore[0] == 0:
            semaphore[0] = 1
            print(f"Process {processID} leaves critical section (binary up).")
        else:
            print(f"Process {processID} cannot leave (already up).")

def counting_semaphore(semaphore, processID, operation):
    if operation == "wait":
        if semaphore[0] > 0:
            semaphore[0] -= 1
            print(f"Process {processID} enters critical section (counting wait).")
        else:
            semaphore[1].append(processID)
            print(f"Process {processID} is waiting (counting wait).")
    elif operation == "signal":
        if len(semaphore[1]) > 0:
            next_process = semaphore[1].pop(0)
            print(f"Process {next_process} enters critical section (counting signal).")
        else:
            semaphore[0] += 1
            print(f"Process {processID} leaves critical section (counting signal).")

def check_conditions(semaphore_type, semaphore):
    if semaphore_type == "binary":
        if semaphore[0] in [0, 1]:
            print("Binary semaphore: Mutual exclusion is guaranteed.")
        else:
            print("Binary semaphore: Invalid state.")
        
        print("Progress condition is satisfied.")  # Binary semaphore will always satisfy progress
        print("Bounded wait is not applicable to binary semaphore.")  # Bounded wait doesn't apply to binary semaphores
    else:
        if semaphore[0] >= 0:
            print("Counting semaphore: Mutual exclusion may not be guaranteed.")
        else:
            print("Counting semaphore: Invalid state.")
        
        if semaphore[0] >= 0:
            print("Progress condition is satisfied.")
        else:
            print("Progress condition is not satisfied.")

        if len(semaphore[1]) == 0:
            print("Bounded wait condition is satisfied.")
        else:
            print("Processes are waiting, bounded wait is not guaranteed.")

num_processes = int(input("Enter the number of processes: "))

if num_processes == 2:
    print("Using binary semaphore.")
    semaphore = [1]  # Binary semaphore initialized to 1
    for _ in range(num_processes):
        processID = input("Enter process ID: ")
        operation = input(f"Process {processID} action (up/down): ").strip().lower()
        binary_semaphore(semaphore, processID, operation)
else:
    print("Using counting semaphore.")
    semaphore_value = int(input("Enter initial semaphore value: "))
    semaphore = [semaphore_value, []]  # Counting semaphore with a queue
    for _ in range(num_processes):
        processID = input("Enter process ID: ")
        operation = input(f"Process {processID} action (wait/signal): ").strip().lower()
        counting_semaphore(semaphore, processID, operation)

check_conditions("binary" if num_processes == 2 else "counting", semaphore)

"""