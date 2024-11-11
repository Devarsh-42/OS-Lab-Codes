import java.util.ArrayList;
import java.util.Scanner;

public class OS_Semaphore {
    public static void binarySemaphore(int[] semaphore, String processID, String operation) {
        if (operation.equals("down")) {
            if (semaphore[0] == 1) {
                semaphore[0] = 0;
                System.out.println("Process " + processID + " enters critical section (binary down).");
            } else {
                System.out.println("Process " + processID + " is waiting (binary down).");
            }
        } else if (operation.equals("up")) {
            if (semaphore[0] == 0) {
                semaphore[0] = 1;
                System.out.println("Process " + processID + " leaves critical section (binary up).");
            } else {
                System.out.println("Process " + processID + " cannot leave (already up).");
            }
        }
    }
    public static void countingSemaphore(int[] semaphore, ArrayList<String> queue, String processID, String operation) {
        if (operation.equals("wait")) {
            if (semaphore[0] > 0) {
                semaphore[0] -= 1;
                System.out.println("Process " + processID + " enters critical section (counting wait).");
            } else {
                queue.add(processID);
                System.out.println("Process " + processID + " is waiting (counting wait).");
            }
        } else if (operation.equals("signal")) {
            if (!queue.isEmpty()) {
                String nextProcess = queue.remove(0);
                System.out.println("Process " + nextProcess + " enters critical section (counting signal).");
            } else {
                semaphore[0] += 1;
                System.out.println("Process " + processID + " leaves critical section (counting signal).");
            }
        }
    }
    public static void checkConditions(String semaphoreType, int[] semaphore, ArrayList<String> queue) {
        if (semaphoreType.equals("binary")) {
            if (semaphore[0] == 0 || semaphore[0] == 1) {
                System.out.println("Binary semaphore: Mutual exclusion is guaranteed.");
            } else {
                System.out.println("Binary semaphore: Invalid state.");
            }
            System.out.println("Progress condition is satisfied.");
            System.out.println("Bounded wait is not applicable to binary semaphore.");
        } else {
            if (semaphore[0] >= 0) {
                System.out.println("Counting semaphore: Mutual exclusion may not be guaranteed.");
            } else {
                System.out.println("Counting semaphore: Invalid state.");
            }
            if (semaphore[0] >= 0) {
                System.out.println("Progress condition is satisfied.");
            } else {
                System.out.println("Progress condition is not satisfied.");
            }
            if (queue.isEmpty()) {
                System.out.println("Bounded wait condition is satisfied.");
            } else {
                System.out.println("Processes are waiting, bounded wait is not guaranteed.");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of processes: ");
        int numProcesses = sc.nextInt();
        sc.nextLine();

        if (numProcesses == 2) {
            System.out.println("Using binary semaphore.");
            int[] semaphore = {1};  // Binary semaphore initialized to 1

            for (int i = 0; i < numProcesses; i++) {
                System.out.print("Enter process ID: ");
                String processID = sc.nextLine();
                System.out.print("Process " + processID + " action (up/down): ");
                String operation = sc.nextLine().trim().toLowerCase();
                binarySemaphore(semaphore, processID, operation);
            }
            checkConditions("binary", semaphore, null);

        } else {
            System.out.println("Using counting semaphore.");
            System.out.print("Enter initial semaphore value: ");
            int semaphoreValue = sc.nextInt();
            sc.nextLine();  // Consume the newline character
            int[] semaphore = {semaphoreValue};
            ArrayList<String> queue = new ArrayList<>();  // Queue for waiting processes

            for (int i = 0; i < numProcesses; i++) {
                System.out.print("Enter process ID: ");
                String processID = sc.nextLine();
                System.out.print("Process " + processID + " action (wait/signal): ");
                String operation = sc.nextLine().trim().toLowerCase();
                countingSemaphore(semaphore, queue, processID, operation);
            }
            checkConditions("counting", semaphore, queue);
        }

        sc.close();
    }
}
