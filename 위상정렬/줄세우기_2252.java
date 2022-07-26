import java.io.*;
import java.util.*;

public class Main {

    static int N, M;

    static ArrayList<ArrayList<Integer>> adjList;
    static int[] priorLinks;

    static ArrayList<Integer> result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        priorLinks = new int[N+1];
        adjList = new ArrayList<>();
        for(int i=0; i<=N; i++) {
            adjList.add(new ArrayList<>());
        }

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int beforeMan = Integer.parseInt(st.nextToken());
            int afterMan = Integer.parseInt(st.nextToken());

            adjList.get(beforeMan).add(afterMan);
            priorLinks[afterMan]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for(int i=1; i<=N; i++) {
            if (priorLinks[i] == 0) {
                q.add(i);
            }
        }

        result = new ArrayList<>();
        while(!q.isEmpty()) {
            int curIdx = q.poll();
            result.add(curIdx);
            for(int nextIdx : adjList.get(curIdx)) {    // 뒤에 있는 노드들에 대하여
                priorLinks[nextIdx]--;
                if(priorLinks[nextIdx] == 0) {
                    q.add(nextIdx);
                }
            }
        }

        for(var node : result) {
            System.out.print(node + " ");
        }

    }
}







