import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static ArrayList<ArrayList<Integer>> adjList;
    static int[] priorLinks;
    static ArrayList<Integer> result;
    static int[] record;
    static int done=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());       // 가수의 수
        M = Integer.parseInt(st.nextToken());       // 보조 PD의 수

        priorLinks = new int[N+1];

        adjList = new ArrayList<>();
        for(int i=0; i<N+1; i++) {
            adjList.add(new ArrayList<>());
        }
        for(int i =0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int memCnt = Integer.parseInt(st.nextToken());
            int beforeIdx = Integer.parseInt(st.nextToken());
            for(int j=1; j < memCnt; j++) {
                int afterIdx = Integer.parseInt(st.nextToken());
                adjList.get(beforeIdx).add(afterIdx);
                priorLinks[afterIdx]++;
                beforeIdx = afterIdx;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for(int i=1; i<=N; i++) {
            if(priorLinks[i] == 0) {
                q.add(i);
            }
        }

        result = new ArrayList<>(1000);
        record = new int[N+1];
        while(!q.isEmpty()) {
            int curIdx = q.poll();
            if(record[curIdx] == 0) {
                result.add(curIdx);
                done++;
            }
            for(int nextIdx : adjList.get(curIdx)) {
                priorLinks[nextIdx]--;
                if(priorLinks[nextIdx] == 0) {
                    q.add(nextIdx);
                }
            }
        }

        if(done < N) {
            System.out.println(0);
        }
        else {
            for(var data : result) {
                System.out.println(data);
            }
        }

    }
}
