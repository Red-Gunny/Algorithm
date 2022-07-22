import java.io.*;
import java.util.*;

public class Main {

    static int N, C;
    static long[] homes;
    static long firstHome = 1000000000, lastHome = 0;

    static long minDist = 1;
    static long maxDist = 0;

    static long answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        homes = new long[N];
        for(int i=0; i<N; i++) {
            homes[i] = Integer.parseInt(br.readLine());
            firstHome = Math.min(firstHome, homes[i]);
            lastHome = Math.max(lastHome, homes[i]);
        }
        maxDist = lastHome - firstHome;

        homes = Arrays.stream(homes)
                .sorted()
                .toArray();

        long cnt = 0;
        while(minDist <= maxDist) {
            cnt = 0;
            boolean flag = false;
            long mid = (minDist + maxDist) / 2;

            int i = 0;
            while(true) {
                for(int j=i; j<N; j++) {
                    if(homes[j] - homes[i] >= mid) {    // 거리가 그 이상임.
                        i = j;
                        cnt++;
                        break;
                    }
                }
                if(i == N-1) {
                    break;
                }
            }


            System.out.println("-----------------------------------------------");
            System.out.println("minDist = " + minDist);
            System.out.println("mid = " + mid);
            System.out.println("maxDist = " + maxDist);
            System.out.println("cnt = " + cnt);
            System.out.println("-----------------------------------------------");
            
            if(cnt < C) {       // 검사해봤더니 C보다 작음 ㅜㅜ -> 거리를 좁혀야 함.
                maxDist = mid - 1;
            }
            else if (cnt > C) {     // 검사해봤더니 C보다 큼 -> 거리를 늘려야함.
                minDist = mid + 1;
                answer = mid;
            }
            else {                      // 딱 맞음... 이거보다 더 거리를 늘릴 순 있지 않을까?
                minDist = mid + 1;
                answer = mid;
            }
        }
        System.out.println(answer);
    }

}

