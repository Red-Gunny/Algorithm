import java.io.*;
import java.util.*;

public class Main {

    static int K;
    static long N;
    static int[] lans;

    static long left=0, right=0;
    static long mid = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        N = Long.parseLong(st.nextToken());
        lans = new int[K];
        for(int i =0; i<K; i++) {
            lans[i] = Integer.parseInt(br.readLine());
            right = Math.max(right, lans[i]);
        }

        long answer = 0;
        while(left <= right) {      // mid+1 / mid-1 이 무조건 되어야 함.
            long cnt = 0;
            mid = (left + right) >>> 1;
            if(mid == 0) {
                mid++;
            }
            for(int lan : lans) {
                cnt += lan / mid;
            }
            if(cnt > N) {       // 랜선을 잘라봤더니 내가 만들기로했던거보다 많아... 이거도 정답에 포함됨 ㄱㅊ
                left = mid + 1;
                answer = Math.max(answer, mid);
            }
            else if (cnt < N) {     // 랜선을 잘라봤더니 내가 만들기로했던거보다 적어..
                right = mid - 1;
            }
            else {
                left = mid + 1;
                answer = Math.max(answer, mid);
            }

            /*System.out.println("left = " + left);
            System.out.println("mid = " + mid);
            System.out.println("right = " + right);

            System.out.println("cnt = " + cnt);
            System.out.println("answer = " + answer);
            Scanner sc = new Scanner(System.in);
            sc.nextInt();*/
        }

        System.out.println(answer);

    }

}

