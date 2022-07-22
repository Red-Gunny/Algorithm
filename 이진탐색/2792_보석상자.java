import java.io.*;
import java.util.*;

public class Main {

    static long N=0;
    static int M=0;
    static long[] stones;

    static long left = 1;
    static long right = 0;
    static long giveOut = 0;

    static long cache = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Long.parseLong(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        stones = new long[M];
        for(int i=0; i<M; i++) {
            stones[i] = Long.parseLong(br.readLine());
            right = Math.max(right, stones[i]);
        }
        // 파싱 완료

        // 나눠줘보기.
        while(left <= right) {
            giveOut = (left + right) / 2;
            long spreadCnt = 0;

            /*for(int i=0; i<M; i++) {
                spreadCnt += stones[i] / giveOut;
                if(stones[i] % giveOut != 0) {
                    spreadCnt++;
                }
            }*/

            for(var stone : stones) {
                long oper = stone;      // 일단 나눠줘 볼 돌 개수
                while(true) {
                    if (oper == 0) {
                        break;
                    }
                    if(oper >= giveOut) {     // 기준 값 보다 많으면
                        oper -= giveOut;        // 나눠줘보고
                        spreadCnt++;            // 개수 증가데스

                    }
                    else {
                        spreadCnt++;            // 그냥 다 소진시캬ㅕ 버리고 개수 증가 대스
                        break;                  // 루프 탈출!
                    }
                }
            }

            /*System.out.println("left = " + left);
            System.out.println("giveOut = " + giveOut);
            System.out.println("right = " + right);
            System.out.println("spreadCnt = " + spreadCnt);

            Scanner sc = new Scanner(System.in);
            sc.nextInt();*/

            // 이제 spreadCnt는 나눠준 개수를 의미해.
            if(spreadCnt > N) {                 // 너무 많은 사람한테 나눠 줌 - 한번에 나눠줄 개수를 증가시켜야됨.
                left = giveOut + 1;
            }
            else if(spreadCnt < N) {               // 너무 적은 사람한테 나눠 줌 - 한번에 나눠줄 개수를 감소시켜야 됨.
                right = giveOut - 1;
                cache = giveOut;
            }
            else {          // 같은 경우는 뭐야... ~> 더 적게 나눠줄 수도 있으니까 더 적게 감소 시켜서 함 검사해봐야됨. 근데
                right = giveOut - 1;
                cache = giveOut;
            }
        }
        System.out.println(cache);
    }

}

