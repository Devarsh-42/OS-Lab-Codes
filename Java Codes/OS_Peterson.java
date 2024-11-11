import java.util.Scanner;

public class OS_Peterson {
    static int turn = 0;
    static boolean[] flag = {false, false};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of processes:");
        int no_processes = sc.nextInt();

        if (no_processes != 2) {
            System.out.println("Invalid input. Peterson's algorithm works for 2 processes only.");
            return;
        }

        System.out.println("Enter the process to be executed (0 for P0, 1 for P1):");
        int process_id = sc.nextInt();

        if (process_id == 0) {
            execute_p0();
        } else if (process_id == 1) {
            execute_p1();
        } else {
            System.out.println("Invalid process ID. Please enter 0 or 1.");
        }
    }

    public static void execute_p0() {
        while (true) {
            flag[0] = true;
            turn = 1;
            long finish = System.currentTimeMillis() + 10000; // 10-second timeout
            while (flag[1] && turn == 1) {
                if (System.currentTimeMillis() >= finish) {
                    System.out.println("Process 0 timed out! Possible mutual exclusion violation.");
                    break;
                }
                System.out.println("Process 0 waiting for the critical section...");
            }

            if (System.currentTimeMillis() < finish) {
                System.out.println("Process 0 entered the critical section");
                Scanner sc = new Scanner(System.in);
                System.out.println("Do you want to context switch the process? (yes/no)");
                String user_cs_response = sc.next();

                if (user_cs_response.equalsIgnoreCase("yes")) {
                    flag[0] = false;
                    execute_p1();
                    break;
                }
            }

            flag[0] = false;
            System.out.println("Process 0 entered the remainder section");
            System.out.println("Process 0 executed!");
        }
    }

    public static void execute_p1() {
        while (true) {
            flag[1] = true;
            turn = 0;
            long finish = System.currentTimeMillis() + 10000; // 10-second timeout
            while (flag[0] && turn == 0) {
                if (System.currentTimeMillis() >= finish) {
                    System.out.println("Process 1 timed out! Possible mutual exclusion violation.");
                    break;
                }
                System.out.println("Process 1 waiting for the critical section...");
            }

            if (System.currentTimeMillis() < finish) {
                System.out.println("Process 1 entered the critical section");
                Scanner sc = new Scanner(System.in);
                System.out.println("Do you want to context switch the process? (yes/no)");
                String user_cs_response = sc.next();

                if (user_cs_response.equalsIgnoreCase("yes")) {
                    flag[1] = false;
                    execute_p0();
                    break;
                }
            }

            flag[1] = false;
            System.out.println("Process 1 entered the remainder section");
            System.out.println("Process 1 executed!");
        }
    }
}
