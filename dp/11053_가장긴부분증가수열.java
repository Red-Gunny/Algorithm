import java.io.*;
import java.util.*;

public class Main {

    static int N=0;
    static int[] A;
    static int[] cntDp;
    static int answer = 0;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N+1];
        cntDp = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=1; i<=N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        cntDp[1] = 1;
        answer = 1;
        for(int i=2; i<=N; i++) {
            cntDp[i] = 1;           // if문 안 걸리는거 방지용.
            for(int j=i-1; j>=1; j--) {
                if(A[j]<A[i]) {        // 지금 타겟 숫자 보다 최대인 값이 작아?
                    if(cntDp[j] >= cntDp[i]) {       // 근데 개수도 많아?
                        cntDp[i] = cntDp[j] + 1;        // 갱신
                        answer = Math.max(answer, cntDp[i]);
                    }
                }
            }
        }
        System.out.println(answer);
    }
}

