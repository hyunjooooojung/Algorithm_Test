import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int N = scanner.nextInt();
        int sumPrice = 0;
        for (int i=0; i<N; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            sumPrice += a*b;
        }
        if (sumPrice == X) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}