import java.io.*;
import java.util.*;

public class Main {

    static int N=0;
    static int[][] dp;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new int[N+1][10];

        for(int i=0; i<10; i++) {
            dp[1][i] = 1;
        }
        if(N==1) {
            System.out.println(10);
            return;
        }

        for(int i=2; i<=N; i++) {
            int sum = 0;
            for(int j=0; j<10; j++) {
                sum += dp[i-1][j];
                dp[i][j] = sum % 10007;
            }
        }
        int answer = 0;
        for(int i=0; i<10; i++) {
            answer += dp[N][i];
        }
        System.out.println(answer % 10007);
    }
}

