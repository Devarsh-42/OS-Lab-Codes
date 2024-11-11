import java.util.Scanner;

public class OS_RoundRobin {
    static void findWaitingTime(int processes[], int n, int bt[], int wt[], int quantum) {
        int rem_bt[] = new int[n];
        for (int i = 0; i < n; i++)
            rem_bt[i] = bt[i];

        int t = 0;
        while (true) {
            boolean done = true;
            for (int i = 0; i < n; i++) {
                if (rem_bt[i] > 0) {
                    done = false;
                    if (rem_bt[i] > quantum) {
                        t += quantum;
                        rem_bt[i] -= quantum;
                    } else {
                        t += rem_bt[i];
                        wt[i] = t - bt[i];
                        rem_bt[i] = 0;
                    }
                }
            }
            if (done)
                break;
        }
    }

    static void findTurnAroundTime(int processes[], int n, int bt[], int wt[], int tat[]) {
        for (int i = 0; i < n; i++)
            tat[i] = bt[i] + wt[i];
    }

    static void findavgTime(int processes[], int n, int bt[], int quantum) {
        int wt[] = new int[n], tat[] = new int[n];
        int total_wt = 0, total_tat = 0;

        findWaitingTime(processes, n, bt, wt, quantum);
        findTurnAroundTime(processes, n, bt, wt, tat);

        System.out.println("Processes  Burst time  Waiting time  Turnaround time");
        for (int i = 0; i < n; i++) {
            total_wt += wt[i];
            total_tat += tat[i];
            System.out.println(" " + processes[i] + "\t\t" + bt[i] + "\t\t" + wt[i] + "\t\t" + tat[i]);
        }
        System.out.println("Average waiting time = " + (float)total_wt / n);
        System.out.println("Average turnaround time = " + (float)total_tat / n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of processes: ");
        int n = sc.nextInt();

        int processes[] = new int[n];
        int burst_time[] = new int[n];

        for (int i = 0; i < n; i++) {
            processes[i] = i + 1;
            System.out.print("Enter burst time for process " + (i + 1) + ": ");
            burst_time[i] = sc.nextInt();
        }

        System.out.print("Enter the time quantum: ");
        int quantum = sc.nextInt();

        findavgTime(processes, n, burst_time, quantum);
    }
}
