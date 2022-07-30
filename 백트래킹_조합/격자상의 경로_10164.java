import java.io.*;
import java.util.*;

public class Main {

    static int sero, garo, mid;

    static int dp[][];
    static int answer = 0;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sero = Integer.parseInt(st.nextToken());
        garo = Integer.parseInt(st.nextToken());
        mid = Integer.parseInt(st.nextToken());

        dp = new int[sero][garo];
        for(int i=0; i<garo; i++) {
            dp[0][i] = 1;
        }
        for(int i=0; i<sero; i++) {
            dp[i][0] = 1;
        }

        int midY=0, midX=0;
        if(mid != 0) {
            int cnt = 1;
            LOOP1:
            for(int i=0; i<sero; i++) {
                for(int j=0; j<garo; j++) {
                    if(cnt == mid) {
                        midY = i;
                        midX = j;
                        break LOOP1;
                    }
                    cnt++;
                }
            }
        }
        else {
            midY = sero-1;
            midX = garo-1;
        }

        for(int i =1; i<= midY; i++) {
            for(int j=1; j<=midX; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        int result1 = dp[midY][midX];       // 0이면 여기서 끝내면 됨.
        int result2 = 0;
        if(mid != 0) {
            for(int i=midX; i<garo; i++) {
                dp[midY][i] = 1;
            }
            for(int i=midY; i<sero; i++) {
                dp[i][midX] = 1;
            }
            for(int i = midY+1; i<sero; i++) {
                for(int j = midX+1; j<garo; j++) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
            result2 = dp[sero-1][garo-1];
            answer = result1 * result2;
        }
        else {
            answer = result1;
        }
        System.out.println(answer);
    }
}


