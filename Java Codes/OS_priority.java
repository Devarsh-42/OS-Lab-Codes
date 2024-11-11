import java.util.Arrays;
import java.util.Scanner;

public class OS_priority {
    public static void main(String[] args) {
        System.out.println("*** Priority Scheduling ***");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number of Process: ");
        int numberOfProcess = sc.nextInt();

        String process[] = new String[numberOfProcess];
        int p = 1;
        for (int i = 0; i < numberOfProcess; i++) {
            process[i] = "P" + p;
            p++;
        }

        System.out.print("Enter Burst Time for " + numberOfProcess + " process: ");
        int burstTime[] = new int[numberOfProcess];
        for (int i = 0; i < numberOfProcess; i++) {
            burstTime[i] = sc.nextInt();
        }

        System.out.print("Enter Priority for " + numberOfProcess + " process: ");
        int priority[] = new int[numberOfProcess];
        for (int i = 0; i < numberOfProcess; i++) {
            priority[i] = sc.nextInt();
        }

        System.out.print("Choose Scheduling: \n1. Non-Preemptive\n2. Preemptive\nEnter your choice: ");
        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                nonPreemptivePriority(process, burstTime, priority, numberOfProcess);
                break;
            case 2:
                preemptivePriority(process, burstTime, priority, numberOfProcess);
                break;
            default:
                System.out.println("Invalid choice!");
        }

        sc.close();
    }

    // Non-Preemptive Priority Scheduling
    public static void nonPreemptivePriority(String[] process, int[] burstTime, int[] priority, int n) {
        // Sorting processes based on priority
        int temp;
        String temp2;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (priority[j] > priority[j + 1]) {
                    temp = priority[j];
                    priority[j] = priority[j + 1];
                    priority[j + 1] = temp;

                    temp = burstTime[j];
                    burstTime[j] = burstTime[j + 1];
                    burstTime[j + 1] = temp;

                    temp2 = process[j];
                    process[j] = process[j + 1];
                    process[j + 1] = temp2;
                }
            }
        }

        int[] TAT = new int[n];
        int[] waitingTime = new int[n];
        int totalWT = 0, totalTAT = 0;

        // Calculating Waiting Time & Turn Around Time
        for (int i = 0; i < n; i++) {
            TAT[i] = burstTime[i] + waitingTime[i];
            if (i < n - 1) {
                waitingTime[i + 1] = TAT[i];
            }
            totalWT += waitingTime[i];
            totalTAT += TAT[i];
        }

        // Display results
        displayResults(process, burstTime, waitingTime, TAT, n, totalWT, totalTAT);
    }

    // Preemptive Priority Scheduling
    public static void preemptivePriority(String[] process, int[] burstTime, int[] priority, int n) {
        int[] remainingTime = new int[n];
        int[] waitingTime = new int[n];
        int[] TAT = new int[n];
        int totalWT = 0, totalTAT = 0;
        boolean[] completed = new boolean[n];

        System.arraycopy(burstTime, 0, remainingTime, 0, n);

        int currentTime = 0, completedProcess = 0;

        while (completedProcess < n) {
            int highestPriorityIndex = -1;
            int highestPriority = Integer.MAX_VALUE;

            for (int i = 0; i < n; i++) {
                if (!completed[i] && priority[i] < highestPriority && remainingTime[i] > 0) {
                    highestPriority = priority[i];
                    highestPriorityIndex = i;
                }
            }

            if (highestPriorityIndex == -1) {
                currentTime++;
                continue;
            }
            remainingTime[highestPriorityIndex]--;
            currentTime++;

            if (remainingTime[highestPriorityIndex] == 0) {
                completed[highestPriorityIndex] = true;
                completedProcess++;

                TAT[highestPriorityIndex] = currentTime;
                waitingTime[highestPriorityIndex] = TAT[highestPriorityIndex] - burstTime[highestPriorityIndex];

                totalWT += waitingTime[highestPriorityIndex];
                totalTAT += TAT[highestPriorityIndex];
            }
        }

        // Display results
        displayResults(process, burstTime, waitingTime, TAT, n, totalWT, totalTAT);
    }

    // Display Results
    public static void displayResults(String[] process, int[] burstTime, int[] waitingTime, int[] TAT, int n, int totalWT, int totalTAT) {
        double avgWT = totalWT / (double) n;
        double avgTAT = totalTAT / (double) n;

        System.out.println("Process     BT      WT        TAT");
        for (int i = 0; i < n; i++) {
            System.out.println(process[i] + "          " + burstTime[i] + "       " + waitingTime[i] + "         " + TAT[i]);
        }

        System.out.println("\nAverage Waiting Time: " + avgWT);
        System.out.println("Average Turn Around Time: " + avgTAT);
    }
}
