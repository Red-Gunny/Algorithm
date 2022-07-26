import java.io.*;
import java.util.*;

public class Main {

    static int N, K;
    static int[] coins;
    static int[] dp;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        coins = new int[N];
        int maxCoin = 0;
        int minCoin = Integer.MAX_VALUE;
        for(int i =0; i<N; i++) {
            coins[i] = Integer.parseInt(br.readLine());
            minCoin = Math.min(minCoin, coins[i]);
            maxCoin = Math.max(maxCoin, coins[i]);
        }
        // 파싱 완료

        int size = Math.max(maxCoin, K);
        dp = new int[size+1];

        for(int i=0; i<=size; i++) {             // 만들 수 없는 경우에 대하여 모두 -1 로 반영.
            dp[i] = Integer.MAX_VALUE - 10;
        }

        for(int coin : coins) {
            dp[coin] = 1;                       // 1인 경우는 무조건...
        }

        for(int i = minCoin; i<=K; i++) {
            for(int coin : coins) {
                if(i - coin < minCoin) {         // 만들 수 없는 경우.
                    continue;
                }
                dp[i] = Math.min(dp[i], dp[i-coin] + 1);     // 예외 처리 필수 !!!
            }
        }

        if (dp[K] == Integer.MAX_VALUE - 10) {
            System.out.println(-1);
        } else {
            System.out.println(dp[K]);
        }
    }

}
