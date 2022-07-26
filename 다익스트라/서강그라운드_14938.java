import java.io.*;
import java.util.*;

public class Main {

    static int N, M, R;
    static int[] items;
    static int answer = 0;
    static ArrayList<ArrayList<Node>> adjList;

    static class Node implements Comparable<Node>{
        int idx;
        int distance;
        Node(int distace, int idx) {
            this.distance = distace;
            this.idx = idx;
        }


        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.distance, o.distance);
        }
    }

    public static int[] dijkstra(int start) {
        int[] distance = new int[N+1];
        for(int i=0; i<=N; i++) {
            distance[i] = 987654321;
        }
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, start));
        distance[start] = 0;
        while(!pq.isEmpty()) {
            Node cur = pq.poll();
            if(cur.distance > distance[cur.idx]) {
                continue;
            }
            for(var next : adjList.get(cur.idx)) {
                int cost = distance[cur.idx] + next.distance;
                if(cost < distance[next.idx]) {
                    distance[next.idx] = cost;
                    pq.add(new Node(cost, next.idx));
                }
            }
        }
        return distance;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());   // 지역의 개수
        M = Integer.parseInt(st.nextToken());   // 수색 범위
        R = Integer.parseInt(st.nextToken());   // 길의 개수
        items = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=N; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        adjList = new ArrayList<>();
        for(int i=0; i<=N; i++) {
            adjList.add(new ArrayList<>());
        }

        for(int i=0; i<R; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            adjList.get(start).add(new Node(weight, end));
            adjList.get(end).add(new Node(weight, start));
        }

        for(int i=1; i<N; i++) {
            int[] distTable = dijkstra(i);
            int maxCnt = 0;
            for(int j=1; j<=N; j++) {
                if(distTable[j] <= M) {
                    maxCnt += items[j];
                }
            }
            answer = Math.max(answer, maxCnt);
        }
        System.out.println(answer);
    }
}
