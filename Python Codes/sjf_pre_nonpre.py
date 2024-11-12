import numpy as np

def sjf_scheduling(processes, schedule_type):
    process_count = len(processes)
    arrival_times = [process[1] for process in processes]
    burst_times = [process[2] for process in processes]
    
    if schedule_type == 1:
        non_preemptive_sjf(process_count, arrival_times, burst_times)
    elif schedule_type == 2:
        preemptive_sjf(process_count, arrival_times, burst_times)
    else:
        print("Invalid scheduling type. Please enter 1 for Non-Preemptive or 2 for Preemptive.")

def non_preemptive_sjf(process_count, arrival_times, burst_times):
    max_value = float('inf')
    arrival_copy = arrival_times.copy()
    burst_copy = burst_times.copy()
    sorted_arrival = sorted(enumerate(arrival_copy), key=lambda x: x[1])

    time_elapsed = 0
    gantt_chart = []
    total_turnaround_time = 0
    total_waiting_time = 0

    for i, arrival_time in sorted_arrival:
        if arrival_time > time_elapsed:
            time_elapsed = arrival_time

        min_burst_index = i
        min_burst = burst_times[min_burst_index]

        for j in range(process_count):
            if arrival_times[j] <= time_elapsed and burst_times[j] < min_burst:
                min_burst = burst_times[j]
                min_burst_index = j

        time_elapsed += burst_times[min_burst_index]
        turnaround_time = time_elapsed - arrival_times[min_burst_index]
        waiting_time = turnaround_time - burst_copy[min_burst_index]

        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

        gantt_chart.append((processes[min_burst_index][0], time_elapsed))

        burst_times[min_burst_index] = max_value

    avg_turnaround_time = total_turnaround_time / process_count
    avg_waiting_time = total_waiting_time / process_count

    print(f"Gantt Chart (Process ID, Time): {gantt_chart}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time = {avg_waiting_time:.2f}")


def preemptive_sjf(process_count, arrival_times, burst_times):
    remaining_time = burst_times.copy()
    completion_times = np.zeros(process_count)
    waiting_times = np.zeros(process_count)
    turnaround_times = np.zeros(process_count)
    is_completed = [False] * process_count

    current_time = 0
    completed = 0

    while completed < process_count:
        min_index = -1
        min_burst = float('inf')

        for i in range(process_count):
            if arrival_times[i] <= current_time and not is_completed[i] and remaining_time[i] < min_burst:
                min_burst = remaining_time[i]
                min_index = i

        if min_index == -1:
            current_time += 1
            continue

        remaining_time[min_index] -= 1
        current_time += 1

        if remaining_time[min_index] == 0:
            completion_times[min_index] = current_time
            turnaround_times[min_index] = completion_times[min_index] - arrival_times[min_index]
            waiting_times[min_index] = turnaround_times[min_index] - burst_times[min_index]
            is_completed[min_index] = True
            completed += 1

    avg_turnaround_time = np.mean(turnaround_times)
    avg_waiting_time = np.mean(waiting_times)

    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time = {avg_waiting_time:.2f}")

n = int(input("Enter the number of Processes: "))
processes = []

for i in range(n):
    pid = input("Enter process id here: ")
    at = int(input(f"Enter the arrival time of {pid}: "))
    bt = int(input(f"Enter the burst time of {pid}: "))
    processes.append((pid, at, bt))
                     
print("Enter the scheduling type:")
print("1 - Non-Preemptive SJF")
print("2 - Preemptive SJF")
schedule_type = int(input("Enter your choice (1 or 2): "))

sjf_scheduling(processes, schedule_type)
