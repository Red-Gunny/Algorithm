import java.io.*;
import java.util.*;

public class Main {

    static int N=0, M=0;
    static int[] parentTable;

    public static int getParent(int idx) {
        if(idx == parentTable[idx]) {
            return idx;
        }
        return parentTable[idx] = getParent(parentTable[idx]);
    }

    public static void unionParent(int first, int second) {
        int parentOfFirst = getParent(first);
        int parentOfSecond = getParent(second);
        if(parentOfFirst > parentOfSecond) {
            parentTable[parentOfFirst] = parentOfSecond;
        }
        else {
            parentTable[parentOfSecond] = parentOfFirst;
        }
    }

    public static boolean findParent(int first, int second) {
        return getParent(first) == getParent(second);
    }

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parentTable = new int[N+1];
        for(int i=0; i<=N; i++) {
            parentTable[i] = i;
        }

        List<String> answerList = new ArrayList<>(M);

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int flag = Integer.parseInt(st.nextToken());
            int num1 = Integer.parseInt(st.nextToken());
            int num2 = Integer.parseInt(st.nextToken());

            if(flag == 0) {
                unionParent(num1, num2);
            }
            else if(flag == 1) {
                if(findParent(num1, num2)) {
                    answerList.add("YES");
                }
                else {
                    answerList.add("NO");
                }
            }
        }
        answerList.forEach(System.out::println);
    }

}
