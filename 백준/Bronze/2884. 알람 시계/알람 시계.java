import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int M = scanner.nextInt();

        if (M >= 45) {
            System.out.printf("%d %d", H, M-45);
        }
        if (M < 45 && H == 0) {
            M += 60;
            H = 23;
            System.out.printf("%d %d", H, M-45);
        }
        if (M < 45) {
            H -= 1;
            M += 60;
            System.out.printf("%d %d", H, M-45);
        }
    }
}