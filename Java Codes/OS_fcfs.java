import java.util.*;

public class OS_fcfs {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of processes:");
        int n = sc.nextInt();
        int[] pid = new int[n]; // Process IDs
        int[] ar = new int[n];  // Arrival times
        int[] bt = new int[n];  // Burst times
        int[] ct = new int[n];  // Completion times
        int[] ta = new int[n];  // Turnaround times
        int[] wt = new int[n];  // Waiting times
        int temp;
        float avgwt = 0, avgta = 0;

        // Input process data
        for (int i = 0; i < n; i++) {
            System.out.println("Enter process " + (i + 1) + " arrival time:");
            ar[i] = sc.nextInt();
            System.out.println("Enter process " + (i + 1) + " burst time:");
            bt[i] = sc.nextInt();
            pid[i] = i + 1;
        }

        // Sorting according to arrival times
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - (i + 1); j++) {
                if (ar[j] > ar[j + 1]) {
                    temp = ar[j];
                    ar[j] = ar[j + 1];
                    ar[j + 1] = temp;
                    temp = bt[j];
                    bt[j] = bt[j + 1];
                    bt[j + 1] = temp;
                    temp = pid[j];
                    pid[j] = pid[j + 1];
                    pid[j + 1] = temp;
                }
            }
        }

        // Non-Preemptive FCFS
        nonPreemptiveFCFS(n, pid, ar, bt, ct, ta, wt);

        // Display the results
        displayResults(n, pid, ar, bt, ct, ta, wt);

        sc.close();
    }

    // Non-preemptive FCFS
    public static void nonPreemptiveFCFS(int n, int[] pid, int[] ar, int[] bt, int[] ct, int[] ta, int[] wt) {
        float avgwt = 0, avgta = 0;

        // Finding completion times
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                ct[i] = ar[i] + bt[i];
            } else {
                if (ar[i] > ct[i - 1]) {
                    ct[i] = ar[i] + bt[i];
                } else {
                    ct[i] = ct[i - 1] + bt[i];
                }
            }
            ta[i] = ct[i] - ar[i]; // Turnaround time = completion time - arrival time
            wt[i] = ta[i] - bt[i]; // Waiting time = turnaround time - burst time
            avgwt += wt[i];         // Total waiting time
            avgta += ta[i];         // Total turnaround time
        }

        System.out.println("\nAverage Waiting Time: " + (avgwt / n));
        System.out.println("Average Turnaround Time: " + (avgta / n));
    }

    // Display the results
    public static void displayResults(int n, int[] pid, int[] ar, int[] bt, int[] ct, int[] ta, int[] wt) {
        System.out.println("\npid  arrival  burst  complete  turn  waiting");
        for (int i = 0; i < n; i++) {
            System.out.println(pid[i] + "\t" + ar[i] + "\t" + bt[i] + "\t" + ct[i] + "\t" + ta[i] + "\t" + wt[i]);
        }
    }
}
