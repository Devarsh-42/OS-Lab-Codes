import time

def peterson_solution():
    process_count = int(input("Enter the number of processes: "))

    if process_count != 2:
        print("Peterson Solution is only for 2 processes.")
        return

    flag = [False, False]
    turn = 0

    print("Enter the condition:")
    print("0 - Normal Condition")
    print("1 - Context Switch Condition")
    condition = int(input("Enter your choice (0 or 1): "))

    if condition not in [0, 1]:
        print("You have chosen an invalid option.")
        return

    if condition == 0:
        process_0(flag, turn, condition)
        process_1(flag, turn)
    else:
        process_0(flag, turn, condition)
        process_1(flag, turn)


def process_0(flag, turn, condition):
    print("Process 0 is running")
    flag[0] = True
    turn = 1

    if condition != 0:
        process_1(flag, turn)

    start_time = time.time()
    while turn == 1 and flag[1]:
        if time.time() - start_time > 10:
            print("Process 0 is ending due to timeout.")
            return

    if time.time() - start_time <= 10:
        print("Process 0 is in Critical Section")

    flag[0] = False
    print("Process 0 has ended")


def process_1(flag, turn):
    print("Process 1 is running")
    flag[1] = True
    turn = 0

    start_time = time.time()
    while turn == 0 and flag[0]:
        if time.time() - start_time > 3:
            print("3 Seconds Wait")
            print("Process 1 is ending due to timeout.")
            return

    if time.time() - start_time <= 10:
        print("Process 1 is in Critical Section")

    flag[1] = False
    print("Process 1 has ended")

peterson_solution()



"""
n = int(input("Enter the number of processes: "))  
turn = 0  
flag = [False, False]  

def p0():
    global turn, flag
    flag[0] = True  
    turn = 1  
    while flag[1] and turn == 1:  
        pass
    print("Process 0 is executing in the critical section.")
    flag[0] = False 

def p1():
    global turn, flag
    flag[1] = True  
    turn = 0  
    while flag[0] and turn == 0:  
        pass
    print("Process 1 is executing in the critical section.")
    flag[1] = False  

def context_switch():
    switch = input("Do you want to context switch the process? (yes/no): ").strip().lower()
    if switch == "yes":
        if pr == "p0":
            print("Context switching to p1...")
            p1()
            print("p0 cannot execute.")
        elif pr == "p1":
            print("Context switching to p0...")
            p0()
            print("p1 cannot execute.")
    elif switch == "no":
        print("No context switch performed.")
    else:
        print("Invalid input. No context switch performed.")

if n == 2:
    pr = input("Enter the process to be executed (p0 or p1): ").strip().lower()
    if pr == "p0":
        p0()
        print("p1 cannot execute.")
        context_switch()
    elif pr == "p1":
        p1()
        print("p0 cannot execute.")
        context_switch()
    else:
        print("Invalid process name. Please enter p0 or p1.")
else:
    print(f"{n} processes are invalid. Enter a valid input.")

"""