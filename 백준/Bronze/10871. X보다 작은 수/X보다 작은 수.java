import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int X = scanner.nextInt();

        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = scanner.nextInt();
        }

        for (int a: arr) {
            if (a < X) {
                System.out.print(a + " ");
            }
        }
    }
}