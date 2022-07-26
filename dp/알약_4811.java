import java.io.*;
import java.util.*;

public class Main {

    static int N;        // 0~N 까지 정수 K개를 더해서 그 합이 N이 되도록...
    static long[][] dp;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            N = Integer.parseInt(br.readLine());
            if(N == 0) {
                return;
            }
            dp = new long[31][31];          // 세로가 W , 가로가  H
            dp[1][0] = dp[0][1] = 1;
            for(int i = 0; i<31; i++) {
                eatPill(i, 0);
            }
            System.out.println(dp[N][0]);
        }
    }

    public static long eatPill(int W, int H) {
        if (dp[W][H] != 0) {
            return dp[W][H];            // W개 H개 있을 때 만들 수 있는 문자열의 수를 기록해쓰면 하는데..
        }
        if(W==0 && H == 0) {
            return 0;
        }
        long mid1=0, mid2=0;
        if(W > 0) {     // 한 알이 1개 이상이라도 있스면
            mid1 = eatPill(W-1, H+1);      // 한개를 반으로 쪼개서 먹었음
        }
        if(H > 0) {
            mid2 = eatPill(W, H-1);
        }
        dp[W][H] = mid1+mid2;
        return dp[W][H];
    }
}





/*System.out.println("==============================================");
            System.out.println("W = " + W);
            System.out.println("H = " + H);
            System.out.println("day = " + day);
            System.out.println("str = " + str);
            System.out.println("==============================================");*/
