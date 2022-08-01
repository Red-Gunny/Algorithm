import java.io.*;
import java.util.*;

public class Main {

    static int N=0, M=0;

    static int[] parent;

    public static int getParent(int idx) {
        if(idx == parent[idx]) {
            return idx;
        }
        return parent[idx] = getParent(parent[idx]);
    }

    public static void unionParent(int first, int second) {
        int firstParent = getParent(first);
        int secondParent = getParent(second);
        if(firstParent < secondParent) {        //
            parent[secondParent] = firstParent;
        }
        else {
            parent[firstParent] = secondParent;
        }
    }

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        parent = new int[N+1];
        for(int i =0; i<=N; i++) {
            parent[i] = i;
        }
        for(int i =1; i<=N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=1; j<=N; j++) {
                int isReachable = Integer.parseInt(st.nextToken());
                if(isReachable == 0) {  // 해당 도시에 도달할 수 없음.
                    continue;
                }
                unionParent(i, j);
            }
        }
        // 파싱 끝
        List<Integer> plans = new ArrayList<>(N);
        StringTokenizer st = new StringTokenizer(br.readLine());
        int norm = Integer.parseInt(st.nextToken());
        int cnt = st.countTokens();
        for(int i=0; i < cnt; i++) {
            int idx = Integer.parseInt(st.nextToken());
            if(getParent(idx) != getParent(norm)) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
