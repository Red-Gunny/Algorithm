import java.io.*;
import java.util.*;

public class Main {

    static int N, K;        // 0~N 까지 정수 K개를 더해서 그 합이 N이 되도록...
    static long[][] dp;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        dp = new long[K+1][N+1];     // 세로축은 사용개수, 가로축은 만드는 숫자.

        for(int i=0; i<=N; i++) {
            dp[1][i] = 1;
        }
        for(int i=1; i<=K; i++) {
            dp[i][0] = 1;
        }

        for(int i = 2; i <= K; i++) {       // i는 사용 개수
            for(int j = 1; j <= N; j++) {     // j는 만드는 숫자.
                for(int p = 0; p <= j; p++) {
                    dp[i][j] =(dp[i][j] + dp[i-1][j-p]) % 1000000000;     // 세로축 : 사용 개수 / 가로축 : 만드는 개수.
                }
            }
        }
        System.out.println(dp[K][N]);
    }
}
