from collections import deque

def round_robin_scheduling(d, tq):
    n = len(d)
    arrival_times = {pid: d[pid]["arrival_time"] for pid in d}
    burst_times = {pid: d[pid]["burst_time"] for pid in d}
    burst_remaining = burst_times.copy()  

    t = 0  
    waiting_time = {pid: 0 for pid in d}
    turnaround_time = {pid: 0 for pid in d}
    is_completed = {pid: False for pid in d}

    queue = deque()  

    for pid in arrival_times:
        if arrival_times[pid] <= t:
            queue.append(pid)

    while queue:
        current_process = queue.popleft()

        if burst_remaining[current_process] > tq:
            t += tq
            burst_remaining[current_process] -= tq

            for pid in arrival_times:
                if (arrival_times[pid] <= t and not is_completed[pid] 
                    and pid not in queue and pid != current_process):
                    queue.append(pid)

            queue.append(current_process)
        
        else:
            t += burst_remaining[current_process]
            burst_remaining[current_process] = 0
            turnaround_time[current_process] = t - arrival_times[current_process]
            waiting_time[current_process] = turnaround_time[current_process] - burst_times[current_process]
            is_completed[current_process] = True

            for pid in arrival_times:
                if (arrival_times[pid] <= t and not is_completed[pid] 
                    and pid not in queue and pid != current_process):
                    queue.append(pid)

    total_waiting_time = sum(waiting_time.values())
    total_turnaround_time = sum(turnaround_time.values())
    
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time = {avg_waiting_time:.2f}")


n = int(input("Enter the number of Processes: "))
tq = int(input("Enter the time quantum: "))
d = {}

for i in range(n):
    pid = input("Enter process id here: ")
    at = int(input(f"Enter the arrival time of {pid}: "))
    bt = int(input(f"Enter the burst time of {pid}: "))
    d[pid] = {"arrival_time": at, "burst_time": bt}

round_robin_scheduling(d, tq)



"""
n = int(input("Enter the number of Processes: "))
tq = int(input("Enter the time quantum: "))
d = {}
l = []

for i in range(n):
    pid = input("Enter process id here: ")
    l.append(pid)
    
    at = int(input(f"Enter the arrival time of {pid}: "))
    bt = int(input(f"Enter the burst time of {pid}: "))
    d[pid] = {"arrival_time": at, "burst_time": bt}

tt = 0 
ttc = 0
wt = 0
tat = 0

proc = []
for pid in l:
    arrival = d[pid]["arrival_time"]
    burst = d[pid]["burst_time"]
    rt = burst
    proc.append([arrival, burst, rt, 0])
    tt += burst

while tt != 0:
    for i in range(len(proc)):
        if proc[i][2] <= tq and proc[i][2] > 0:
            ttc += proc[i][2]
            tt -= proc[i][2]
            proc[i][2] = 0 
        elif proc[i][2] > 0:
            proc[i][2] -= tq
            tt -= tq
            ttc += tq
        
        if proc[i][2] == 0 and proc[i][3] != 1:
           
            wt += ttc - proc[i][0] - proc[i][1]
            tat += ttc - proc[i][0]
            proc[i][3] = 1  

print("Avg Waiting Time is:", (wt/n))
print("Avg Turnaround Time is:", (tat/n))

"""