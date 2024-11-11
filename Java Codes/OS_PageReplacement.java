import java.util.*;

public class OS_PageReplacement {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of frames");
        int frames = sc.nextInt();
        System.out.println("Enter the length of string");
        int length = sc.nextInt();

        double hit = 0;

        int[] refString = new int[length];
        int[] frameArr = new int[frames];

        System.out.println("Enter the reference string");
        for (int i = 0; i < length; i++) {
            refString[i] = sc.nextInt();
        }
        System.out.println();
        int index = 0;
        for (int i = 0; i < frameArr.length; i++) {
            frameArr[i] = -1;
        }
        System.out.println("Page Table : ");
        for (int i = 0; i < length; i++) {
            boolean check = false;
            for (int j = 0; j < frameArr.length; j++) {
                if (refString[i] == frameArr[j]) {
                    check = true;
                }
            }
            if (check) {
                hit += 1;
                System.out.println(Arrays.toString(frameArr));
                continue;
            } else {
                frameArr[index % frames] = refString[i];
                System.out.println(Arrays.toString(frameArr));
                index++;
            }
        }
        double hitR = hit / length;
        System.out.println();
        System.out.println("No. of Hits : " + hit);
        System.out.println("Hit Ratio : " + hitR);
    }
}