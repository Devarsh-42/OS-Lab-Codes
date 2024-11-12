import java.util.Scanner;

public class OS_Banker_Algorithm {
    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);

        // Input number of processes and resources
        System.out.print("Enter no of processes: ");
        int n = sc.nextInt();
        System.out.print("Enter no of resources: ");
        int r = sc.nextInt();

        System.out.println("Enter available resources:");
        int[] available = new int[r];
        for (int i = 0; i < r; i++) {
            available[i] = sc.nextInt();
        }

        int[][] max = new int[n][r];
        int[][] allocation = new int[n][r];
        int[][] need = new int[n][r];

        // Input maximum resources for each process
        System.out.println("Enter the maximum resources for each process:");
        for (int i = 0; i < n; i++) {
            System.out.println("Process " + (i + 1) + ":");
            for (int j = 0; j < r; j++) {
                max[i][j] = sc.nextInt();
            }
        }

        // Input allocated resources for each process
        System.out.println("Enter the allocated resources for each process:");
        for (int i = 0; i < n; i++) {
            System.out.println("Process " + (i + 1) + ":");
            for (int j = 0; j < r; j++) {
                allocation[i][j] = sc.nextInt();
            }
        }

        // Calculate the need matrix (Need = Max - Allocation)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < r; j++) {
                need[i][j] = max[i][j] - allocation[i][j];
            }
        }

        // Display Need matrix
        System.out.println("Need matrix is:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < r; j++) {
                System.out.print(need[i][j] + " ");
            }
            System.out.println();
        }

        // Check for safe sequence
        int[] safeSequence = new int[n];
        if (isSafe(n, r, available, allocation, need, safeSequence)) {
            System.out.println("The system is in a safe state.");
            System.out.print("Safe sequence: ");
            for (int i = 0; i < n; i++) {
                System.out.print("P" + (safeSequence[i] + 1) + " ");
            }
            System.out.println();
        } else {
            System.out.println("The system is not in a safe state.");
        }

        sc.close();
    }

    static boolean isSafe(int n, int r, int[] available, int[][] allocation, int[][] need, int[] safeSequence) {
        boolean[] finish = new boolean[n];
        int[] work = new int[r];

        // Initialize work array to available resources
        for (int i = 0; i < r; i++) {
            work[i] = available[i];
        }

        int count = 0;  // Track the number of processes finished in a safe sequence

        while (count < n) {
            boolean found = false;
            for (int i = 0; i < n; i++) {
                if (!finish[i]) {
                    // Check if the process's needs can be satisfied with available resources
                    int j;
                    for (j = 0; j < r; j++) {
                        if (need[i][j] > work[j]) {
                            break;
                        }
                    }

                    // If all needs of process i can be satisfied, execute it
                    if (j == r) {
                        // Add the allocated resources of process i back to available (work array)
                        for (int k = 0; k < r; k++) {
                            work[k] += allocation[i][k];
                        }

                        // Mark the process as finished
                        finish[i] = true;
                        safeSequence[count++] = i;  // Store the process in the safe sequence
                        found = true;
                    }
                }
            }
            if (!found) {
                return false;
            }
        }
        return true;
    }
}
