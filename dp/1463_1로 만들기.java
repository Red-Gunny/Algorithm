import java.io.*;
import java.util.*;

public class Main {

    static int X=0;
    static int[] dp;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        X = Integer.parseInt(br.readLine());
        dp = new int[X+1];
        dp[1] = 0;
        if(X <= 1) {
            System.out.println(0);
            return;
        }
        else if(X <= 3) {
            System.out.println(1);
            return;
        }
        dp[2]=1;
        dp[3]=1;
        for(int i =4; i<=X; i++) {
            dp[i] = Math.min(dp[(int)i/3]+1 + (i%3), dp[(int)i/2]+1 + (i%2));
            dp[i] = Math.min(dp[i], dp[i-1]+1);
        }
        System.out.println(dp[X]);
    }
}

