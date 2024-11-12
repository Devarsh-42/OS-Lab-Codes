def priority_scheduling(d, p, scheduling_type):
    process_count = len(d)
    arrival_times = {pid: d[pid][0] for pid in d}
    burst_times = {pid: d[pid][1] for pid in d}
    priorities = p.copy()
    
    if scheduling_type == 1:
        non_preemptive_priority(process_count, arrival_times, burst_times, priorities)
    elif scheduling_type == 2:
        preemptive_priority(process_count, arrival_times, burst_times, priorities)
    else:
        print("Invalid scheduling type. Please enter 1 for Non-Preemptive or 2 for Preemptive.")


def non_preemptive_priority(process_count, arrival_times, burst_times, priorities):
    time_elapsed = 0
    gantt_chart = []
    total_turnaround_time = 0
    total_waiting_time = 0
    is_completed = {pid: False for pid in arrival_times}
    sorted_priorities = sorted(priorities.items(), key=lambda x: x[1])

    for _ in range(process_count):
        selected_process = None
        
        for pid, pr in sorted_priorities:
            if arrival_times[pid] <= time_elapsed and not is_completed[pid]:
                if selected_process is None or priorities[pid] < priorities[selected_process]:
                    selected_process = pid
        
        if selected_process:
            time_elapsed += burst_times[selected_process]
            turnaround_time = time_elapsed - arrival_times[selected_process]
            waiting_time = turnaround_time - burst_times[selected_process]
            
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

            gantt_chart.append((selected_process, time_elapsed))
            is_completed[selected_process] = True
        else:
            time_elapsed += 1

    avg_turnaround_time = total_turnaround_time / process_count
    avg_waiting_time = total_waiting_time / process_count

    print(f"Gantt Chart (Process ID, Time): {gantt_chart}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time = {avg_waiting_time:.2f}")


def preemptive_priority(process_count, arrival_times, burst_times, priorities):
    remaining_time = burst_times.copy()
    completion_times = {}
    turnaround_times = {}
    waiting_times = {}
    is_completed = {pid: False for pid in arrival_times}

    current_time = 0
    completed = 0

    while completed < process_count:
        selected_process = None
        
        for pid in arrival_times:
            if arrival_times[pid] <= current_time and not is_completed[pid]:
                if selected_process is None or priorities[pid] < priorities[selected_process]:
                    selected_process = pid

        if selected_process:
            remaining_time[selected_process] -= 1
            current_time += 1
            
            if remaining_time[selected_process] == 0:
                completion_times[selected_process] = current_time
                turnaround_times[selected_process] = completion_times[selected_process] - arrival_times[selected_process]
                waiting_times[selected_process] = turnaround_times[selected_process] - burst_times[selected_process]
                is_completed[selected_process] = True
                completed += 1
        else:
            current_time += 1

    avg_turnaround_time = sum(turnaround_times.values()) / process_count
    avg_waiting_time = sum(waiting_times.values()) / process_count

    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time = {avg_waiting_time:.2f}")

n = int(input("Enter the number of Processes: "))
d = {}
p = {}

for i in range(n):
    pid = input("Enter process id here: ")
    at = int(input(f"Enter the arrival time of {pid}: "))
    bt = int(input(f"Enter the burst time of {pid}: "))
    priority = int(input(f"Enter the priority of {pid} (lower number means higher priority): "))
    d[pid] = (at, bt)
    p[pid] = priority

print("Enter the scheduling type:")
print("1 - Non-Preemptive Priority")
print("2 - Preemptive Priority")
scheduling_type = int(input("Enter your choice (1 or 2): "))

priority_scheduling(d, p, scheduling_type)


"""
stpr=sorted process
slpr=selected process
cltime=completion time
cutime=current time
avpr=available process
"""
"""
n = int(input("Enter the number of Processes: "))
d = {}
l = []
p = {}

for i in range(n):
    pid = input("Enter process id here: ")
    l.append(pid)

    at = int(input(f"Enter the arrival time of {pid}: "))
    bt = int(input(f"Enter the burst time of {pid}: "))
    priority = int(input(f"Enter the priority of {pid} (lower number means higher priority): "))

    d.update({pid: (at, bt)})
    p.update({pid: priority})

print("Process Arrival and Burst Times:", d)
print("Process IDs:", l)
print("Priorities:", p)


stpr = sorted(l, key=lambda x: (d[x][0], p[x]))

print("Sorted Process Order based on Arrival Time and Priority:", stpr)


cltime = {}
cutime = 0
tat = {}
wt = {}

while stpr:

    avpr = [pid for pid in stpr if d[pid][0] <= cutime]

    if avpr:
        slpr = min(avpr, key=lambda x: p[x])
    
    else:
        cutime = d[stpr[0]][0]
        slpr = stpr[0]
    
    at, bt = d[slpr]
    cutime = max(cutime, at) + bt
    cltime[slpr] = cutime
    tat[slpr] = cltime[slpr] - at
    wt[slpr] = tat[slpr] - bt

    stpr.remove(slpr)

avg_tat = sum(tat.values()) / n
avg_wt = sum(wt.values()) / n

print(f"Completion Times: {cltime}")
print(f"Turnaround Times: {tat}")
print(f"Waiting Times: {wt}")
print(f"The average Turnaround time is: {avg_tat}")
print(f"The average Waiting time is: {avg_wt}")

"""
