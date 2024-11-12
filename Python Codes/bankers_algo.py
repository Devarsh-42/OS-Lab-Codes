import numpy as np

def bankers_algorithm():
    p = int(input("Enter the number of processes: "))
    r = int(input("Enter the number of resources: "))

    total = list(map(int, input("Enter the total resources for each resource type (space-separated): ").split()))

    allocation = []
    print("Enter the allocation matrix (allocated resources for each process):")
    for i in range(p):
        row = list(map(int, input(f"Process {i + 1} allocation: ").split()))
        allocation.append(row)

    max_need = []
    print("Enter the max need matrix (maximum resources required by each process):")
    for i in range(p):
        row = list(map(int, input(f"Process {i + 1} max need: ").split()))
        max_need.append(row)

    allocation = np.array(allocation)
    max_need = np.array(max_need)
    total = np.array(total)

    remaining = max_need - allocation

    sum_allocation = allocation.sum(axis=0)
    available = total - sum_allocation

    print("\nInitial Allocation Matrix:")
    print(allocation)
    print("\nMaximum Need Matrix:")
    print(max_need)
    print("\nRemaining Need Matrix:")
    print(remaining)
    print("\nInitial Available Resources:", available)

    safe_sequence = []
    finish = [False] * p  

    while len(safe_sequence) < p: 
        allocated_this_round = False

        for i in range(p):
            if not finish[i]:
                if all(remaining[i] <= available):
                    print(f"\nProcess {i + 1} is able to complete; allocating resources.")
                    available += allocation[i]  
                    safe_sequence.append(i + 1) 
                    finish[i] = True  
                    allocated_this_round = True
                    print("Current Available Resources after allocation:", available)

        if not allocated_this_round:
            print("\nNo safe sequence found. System is in an unsafe state.")
            return
        
    print("\nSafe Sequence Found:", safe_sequence)

bankers_algorithm()

"""
def is_safe(n, r, available, allocation, need):
    finish = [False] * n  
    work = available[:]  
    safe_sequence = []  
    count = 0

    while count < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(r)):
                    for k in range(r):
                        work[k] += allocation[i][k]

                    finish[i] = True
                   
                    safe_sequence.append(i)
                    found = True
                    count += 1

        if not found:
            return False, []
    return True, safe_sequence 


def banker_algorithm():
    n = int(input("Enter no of processes: "))
    r = int(input("Enter no of resources: "))

    r_type = input("Enter type of resources\n\t1. CPU\n\t2. Memory\n\t3. Printer: ")
    if r_type == "CPU":
        print("Resource Type: CPU")
    elif r_type == "Memory":
        print("Resource Type: Memory")
    elif r_type == "Printer":
        print("Resource Type: Printer")
    else:
        print("Invalid resource type. Exiting.")
        return

    available = [10,5,7]

    max_resources = [[0] * r for _ in range(n)]
    allocation = [[0] * r for _ in range(n)]
    need = [[0] * r for _ in range(n)]

    print("Enter the maximum resources for each process (space-separated):")
    for i in range(n):
        print(f"Process {i + 1}:")
        max_resources[i] = list(map(int, input().split()))

    print("Enter the allocated resources for each process (space-separated):")
    for i in range(n):
        print(f"Process {i + 1}:")
        allocation[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(r):
            need[i][j] = max_resources[i][j] - allocation[i][j]

    print("Need matrix is:")
    for row in need:
        print(" ".join(map(str, row)))

    safe, safe_sequence = is_safe(n, r, available, allocation, need)

    if safe:
        print("The system is in a safe state.")
        print("Safe sequence is:", " -> ".join([f"P{i+1}" for i in safe_sequence]))
    else:
        print("The system is not in a safe state. No safe sequence exists.")

banker_algorithm()
"""