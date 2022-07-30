import java.io.*;
import java.util.*;

public class Main {

    static int N=0;
    static int[] dp;
    static int[] stairs;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new int[N+1];
        stairs = new int[N+1];
        for(int i=1; i<=N; i++) {
            int weight = Integer.parseInt(br.readLine());
            stairs[i] = weight;
        }
        dp[1] = stairs[1];
        if(N == 1) {
            System.out.println(stairs[1]);
            return;
        }
        dp[2] = stairs[1] + stairs[2];
        if(N==2) {
            System.out.println(dp[2]);
            return;
        }
        dp[3] = Math.max(stairs[1] + stairs[3], stairs[2]+stairs[3]);
        if(N==3) {
            System.out.println(dp[3]);
            return;
        }
        for(int i=4; i<=N; i++) {
            dp[i] = Math.max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]);
        }
        System.out.println(dp[N]);
    }
}

