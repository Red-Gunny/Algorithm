import java.io.*;
import java.util.*;

public class Main {

    static int N, C;

    static long[] homes;

    static long left=0, right=0;
    static long dist = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        homes = new long[N];
        for(int i =0; i<N; i++) {
            homes[i] = Integer.parseInt(br.readLine());
            right = Math.max(right, homes[i]);
        }

        homes = Arrays.stream(homes)
                .sorted()
                .toArray();

        long answer = 0;
        while(left <= right) {
            dist = (left+right) >>> 1;
            long normHome = homes[0];
            int wifiCnt = 1;
            for(long home: homes) {
                if(normHome + dist <= home) {       // 기준점 + 공유기 거리. 가 지금 좌표보다 길어?
                    wifiCnt++;
                    normHome = home;
                }
            }

            if(wifiCnt > C) {       // 와이파이 설치 개수가 예정보다 커. 그러면 설치개수 작아지도록 사이거리를 크게해ㅑ지
                left = dist + 1;
                answer = Math.max(answer, dist);
            }
            else if(wifiCnt < C) {      // 와이파이 설치 개수가 예정보다 작아. 그러면 설치개수 커지도록 서이가리를 좁혀야 돼.
                right = dist - 1;
            }
            else {      // Upper Bound 때문에 혹시나 더 있을 지 모르니까. 답만 기록홰오ㅑ.
                left = dist + 1;
                answer = Math.max(answer, dist);
            }

            /*System.out.println("left = " + left);
            System.out.println("dist = " + dist);
            System.out.println("right = " + right);

            System.out.println("wifiCnt = " + wifiCnt);*/

        }
        //System.out.println("answer = " + answer);
        System.out.print(answer);
    }

}

