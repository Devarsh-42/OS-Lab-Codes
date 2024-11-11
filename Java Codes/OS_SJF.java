import java.util.Arrays;
import java.util.Scanner;

public class OS_SJF {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of processes:");
        int n = sc.nextInt();
        int[] pid = new int[n];
        int[] at = new int[n];
        int[] bt = new int[n];
        int[] ct = new int[n];
        int[] ta = new int[n];
        int[] wt = new int[n];
        int[] f = new int[n];
        int[] k = new int[n];

        for(int i = 0; i < n; ++i) {
            pid[i] = i + 1;
            System.out.println("Enter process " + (i + 1) + " arrival time:");
            at[i] = sc.nextInt();
            System.out.println("Enter process " + (i + 1) + " burst time:");
            bt[i] = sc.nextInt();
            k[i] = bt[i];
            f[i] = 0;
        }

        nonPreemptiveSJF(n, pid, at, bt, ct, ta, wt, k, f);
        displayResults(n, pid, at, k, ct, ta, wt);
        Arrays.fill(f, 0);
        System.arraycopy(k, 0, bt, 0, n);
        preemptiveSJF(n, pid, at, bt, ct, ta, wt, k, f);
        displayResults(n, pid, at, k, ct, ta, wt);
        sc.close();
    }

    public static void nonPreemptiveSJF(int n, int[] pid, int[] at, int[] bt, int[] ct, int[] ta, int[] wt, int[] k, int[] f) {
        int st = 0;
        int tot = 0;
        float avgwt = 0.0F;
        float avgta = 0.0F;

        while(true) {
            int c = n;
            int min = 99;
            if (tot == n) {
                return;
            }

            for(int i = 0; i < n; ++i) {
                if (at[i] <= st && f[i] == 0 && bt[i] < min) {
                    min = bt[i];
                    c = i;
                }
            }

            if (c == n) {
                ++st;
            } else {
                st += bt[c];
                ct[c] = st;
                ta[c] = ct[c] - at[c];
                wt[c] = ta[c] - k[c];
                f[c] = 1;
                ++tot;
            }
        }
    }

    public static void preemptiveSJF(int n, int[] pid, int[] at, int[] bt, int[] ct, int[] ta, int[] wt, int[] k, int[] f) {
        int st = 0;
        int tot = 0;
        float avgwt = 0.0F;
        float avgta = 0.0F;

        while(true) {
            int min = 99;
            int c = n;
            if (tot == n) {
                return;
            }

            for(int i = 0; i < n; ++i) {
                if (at[i] <= st && f[i] == 0 && bt[i] < min) {
                    min = bt[i];
                    c = i;
                }
            }

            if (c == n) {
                ++st;
            } else {
                int var10002 = bt[c]--;
                ++st;
                if (bt[c] == 0) {
                    ct[c] = st;
                    ta[c] = ct[c] - at[c];
                    wt[c] = ta[c] - k[c];
                    f[c] = 1;
                    ++tot;
                }
            }
        }
    }

    public static void displayResults(int n, int[] pid, int[] at, int[] k, int[] ct, int[] ta, int[] wt) {
        float avgwt = 0.0F;
        float avgta = 0.0F;
        System.out.println("PID\tArrival\tBurst\tComplete\tTurnaround\tWaiting");

        for(int i = 0; i < n; ++i) {
            avgwt += (float)wt[i];
            avgta += (float)ta[i];
            System.out.println(pid[i] + "\t" + at[i] + "\t" + k[i] + "\t" + ct[i] + "\t\t" + ta[i] + "\t\t" + wt[i]);
        }

        System.out.println("\nAverage Turnaround Time: " + avgta / (float)n);
        System.out.println("Average Waiting Time: " + avgwt / (float)n + "\n");
    }
}
