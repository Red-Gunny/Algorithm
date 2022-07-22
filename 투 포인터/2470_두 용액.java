import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static long[] liquors;

    static int left, right;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        liquors = new long[N];
        for(int i =0; i<N; i++) {
            liquors[i] = Integer.parseInt(st.nextToken());
        }
        liquors = Arrays.stream(liquors)
                .sorted()
                .toArray();

        left = 0;
        right = N-1;
        long sum =0;

        int recordLeft = 0;
        int recordRight = 0;
        long cache = 2000000000;
        while(left < right) {
            sum = liquors[left] + liquors[right];

            if(Math.abs(sum) < Math.abs(cache)) {
                cache = sum;
                recordLeft = (int)liquors[left];
                recordRight = (int)liquors[right];
            }
            if (sum > 0) {      // 양수야. 그럼 양수이동
                right--;
            }
            else if(sum < 0) {      // 음수야. 그러면 음수 이동.
                left++;
            }
            else {
                break;
            }

        }
        System.out.print(recordLeft + " " + recordRight);
    }

}

