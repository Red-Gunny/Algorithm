import java.io.*;
import java.util.*;

public class Main {

    static int N = 0;
    static int M = 0;

    static long[] dataArr;
    static int start=0, end=0;
    static long answer = Integer.MAX_VALUE;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        dataArr = new long[N];
        for(int i=0; i<N; i++) {
            dataArr[i] = Long.parseLong(br.readLine());
        }
        Arrays.sort(dataArr);


        while(start<N && end<N) {
            long subtractValue = dataArr[end] - dataArr[start];
            if(subtractValue < M) {
                end++;
            }
            else if (subtractValue > M) {       // M보다 커~~ ㅠㅠ 스타트를 옮겨라
                answer = Math.min(answer, subtractValue);
                start++;
            }
            else {      // 이거보다 더 작을 수는 없지~
                System.out.println(M);
                return;
            }
        }
        while(start<N) {
            long subtractValue = dataArr[N-1] - dataArr[start];
            if(subtractValue >= M) {
                answer = Math.min(answer, subtractValue);
                start++;
            }
            else {
                break;
            }
        }
        System.out.println(answer);

    }

}
