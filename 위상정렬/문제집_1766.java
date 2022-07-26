import java.io.*;
import java.util.*;

public class Main {

    static int N, M;

    static ArrayList<ArrayList<Integer>> adjList;
    static int[] priorList;
    static ArrayList<Integer> result;
    static boolean[] already;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());   // 문제의 수
        M = Integer.parseInt(st.nextToken());       // 들어올 데이터 수

        priorList = new int[N+1];
        adjList = new ArrayList<>();
        for(int i=0; i<=N; i++) {
            adjList.add(new ArrayList<>());
        }

        for(int i =0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int before = Integer.parseInt(st.nextToken());
            int after = Integer.parseInt(st.nextToken());
            adjList.get(before).add(after);     // 후행노드를 넣는 것임 !!
            priorList[after]++;                 // 후행노드의 앞에 노드 수 증가
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=1; i<=N; i++) {
            if(priorList[i] == 0) {     // 앞선 노드가 없으면 pq에 넣는다.
                pq.add(i);
            }
        }

        result = new ArrayList<>();
        already = new boolean[N+1];
        while(!pq.isEmpty()) {
            int curIdx = pq.poll();
            if(!already[curIdx]) {
                result.add(curIdx);
                already[curIdx] = true;
            }

            for(var nextIdx : adjList.get(curIdx)) {        // 현재 노드 기준 모든 후행노드들에 대하여
                priorList[nextIdx]--;                       // 감소시켜봐~
                if(priorList[nextIdx] == 0) {                   // 0 이면 넣으라고
                    pq.add(nextIdx);
                }
            }
        }

        for(int idx : result) {
            System.out.print(idx + " ");
        }
    }
}
