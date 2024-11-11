import java.util.concurrent.Semaphore;

public class OS_Reader_Writer_Problem {
    static int readCount = 0; //number of readers
    static Semaphore resource = new Semaphore(1); //shared resource semaphore
    static Semaphore readLock = new Semaphore(1); // Semaphore for the readers
    static class Reader extends Thread {
        public void run() {
            try {
                readLock.acquire();
                readCount++;
                if (readCount == 1) {
                    resource.acquire();
                }
                readLock.release();
                System.out.println(Thread.currentThread().getName() + " is reading.");
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName() + " has finished reading.");

                readLock.acquire();
                readCount--;
                if (readCount == 0) {
                    resource.release();
                }
                readLock.release();
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    static class Writer extends Thread {
        public void run() {
            try {
                resource.acquire();
                System.out.println(Thread.currentThread().getName() + " is writing.");
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName() + " has finished writing.");
                resource.release();
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    public static void main(String[] args) {
        Reader reader1 = new Reader();
        Reader reader2 = new Reader();
        Writer writer1 = new Writer();
        Writer writer2 = new Writer();

        reader1.start();
        writer1.start();
        reader2.start();
        writer2.start();
    }
}