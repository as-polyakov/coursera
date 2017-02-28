import java.util.*;

public class Lcm {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        long a = s.nextLong();
        long b = s.nextLong();
        System.out.println(a * b + " " + a * b / gcd(a, b));
    }
    private static long gcd(long a, long b) {
        if(b == 0)
            return a;
        return gcd(b, a % b);
    }
}
