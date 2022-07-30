import java.io.*;
import java.util.*;

public class Main {

    static int N = 0;
    static ArrayList<ArrayList<Node>> adjList;

    static ArrayList<Integer> targets;
    static int answer = 0;

    static int target = 0;


    static int midAnswer = 0;
    static int midIdx = 0;

    static class Node {
        int idx;
        int dist;
        Node(int idx, int dist) {
            this.idx = idx;
            this.dist = dist;
        }
    }

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        adjList = new ArrayList<>();
        for(int i =0; i<=N; i++) {
            adjList.add(new ArrayList<>());
        }

        targets = new ArrayList<>(N+1);

        for(int i =0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int curIdx = Integer.parseInt(st.nextToken());
            int leafCheck = 0;
            Node before = null;
            while(true) {
                int adjIdx = Integer.parseInt(st.nextToken());
                if(adjIdx == -1) {      // 끝이야~
                    break;
                }
                int dist = Integer.parseInt(st.nextToken());
                before = new Node(adjIdx, dist);
                adjList.get(curIdx).add(before);
                leafCheck++;
            }
            if(leafCheck == 0) {        // 혼자 독단으로 있는 경우 예외 처리 필.
                continue;
            }
            if(leafCheck == 1) {        // 그냥 혼자잇는경우 예외처리 필요함.
                targets.add(curIdx);        // targets 사이즈 0 인 경우 예외처리 필
            }
        }

        if(targets.size() == 0) {           // 그냥 혼자 섬으로들만 있는 경우
            System.out.println(0);
            return;
        }

        boolean[] visited = new boolean[N+1];
        visited[1] = true;
        dfs(1, visited, 0);
        visited = new boolean[N+1];
        visited[midIdx] = true;
        dfs(midIdx, visited, 0);
        System.out.println(midAnswer);
    }

    // 2nd 인자 : 첫 스택에서 시작 노드가 들가야함.
    // 4th 인자 : 처음 부를때 (main) 0 들어가야함.
    public static void dfs(int cur, boolean[] visited, int distance) {
        if(distance > midAnswer) {  // 갱신대쓰
            midAnswer = distance;
            midIdx = cur;
        }
        for(Node adjs : adjList.get(cur)) {     // 현재 모든 붙어있는 노드들에 대하여
            if(visited[adjs.idx]) {     // 이미 방문해쓰면
                continue;                 // 무시
            }
            visited[adjs.idx] = true;       // 방문 처리를 해주고
/*            System.out.println("before = " + distance);
            System.out.println("adjs.dist = " + adjs.dist);
            System.out.println("distance = " + (distance + adjs.dist));*/
            dfs(adjs.idx, visited, distance + adjs.dist);
        }
    }
}


/*for(int i=0; i<targets.size(); i++) {
            for(int j=i+1; j<targets.size(); j++) {
                boolean[] visited = new boolean[N+1];
                int tar1 = targets.get(i);
                target = targets.get(j);        // 최종 도달지
                visited[tar1] = true;
                dfs(tar1, visited, 0);      // midAnswer이 바뀜
                answer = Math.max(answer, midAnswer);
                //answer = Math.max(answer, dfs(tar1, visited, 0));
            }
}*/
