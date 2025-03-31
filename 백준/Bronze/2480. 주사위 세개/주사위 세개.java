import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        if (a == b && b == c) {
            System.out.println(10000 + a * 1000);
        }
        else if (a == b || a == c) {
            System.out.println(1000 + a * 100);
        }
        else if (b == c) {
            System.out.println(1000 + b * 100);
        }
        else {
            int max = Math.max(a, Math.max(b, c));
            System.out.println(100*max);
        }
    }
}