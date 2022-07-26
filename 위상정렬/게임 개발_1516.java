import java.io.*;
import java.util.*;

public class Main {

    static int N = 0;
    static int[] constructTime;
    static int[] completeTime;
    static ArrayList<ArrayList<Integer>> mustConList; // mustConList
    static ArrayList<ArrayList<Integer>> adjList;
    static int[] priorLink;

    static int answer = 0;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        constructTime = new int[N+1];       // 개별 건물의 짓는데 걸리는 시간
        completeTime = new int[N+1];        // 다 짓는데 걸리는 절대 시간
        priorLink = new int[N+1];           // 앞선 노드를 이제 확인할거임
        mustConList = new ArrayList<>();        // 인접 리스트
        adjList = new ArrayList<>();            // 내 뒤에 있는 노드는 무엇이니?
        for(int i=0; i<=N; i++) {
            mustConList.add(new ArrayList<>());
            adjList.add(new ArrayList<>());
        }

        Queue<Integer> q = new LinkedList<>();

        for(int i=1; i<=N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());        // 한줄을 읽었어.
            int time = Integer.parseInt(st.nextToken());        // 건물 1개 지어지는 시간
            constructTime[i] = time;
            /*System.out.println("==========================================");
            System.out.println(st.countTokens());
            System.out.println("i = " + i);
            System.out.println("==========================================");*/
            while(true) {
                /*System.out.println("루프 몇번이나 돌았길래 이지랄");
                System.out.println("time = " + time);*/

                int before = Integer.parseInt(st.nextToken());
                if(before == -1) {      // 탈출 조건
                    break;
                }
                priorLink[i]++;                 // "앞선 노드가 몇개니?" 를  나타낸다.
                mustConList.get(i).add(before);     // "지금 내 노드를 지으려면 앞에 노드는 무엇을 지어야하니?"
                adjList.get(before).add(i);         // 내 뒤에 있는 노드는 무엇일까?~
            }

            if(priorLink[i] == 0) {        // 0이면 삽입
                q.add(i);
            }
        }

        while(!q.isEmpty()) {
            int conIdx = q.poll();      // 이제 앞선 노드가 없는 것들 pop

            // 선행 건축물이 없어도 괜찮음.
            int startTime = 0;
            for(int beforeIdx : mustConList.get(conIdx)) {      // 먼저 지어야하는 선행 건축물들에 대하여..
                startTime = Math.max(startTime, completeTime[beforeIdx]);       // 가장 오래 걸리는 건 무엇이니?
            }
            int endTime = startTime + constructTime[conIdx];        // 다 지으려면 이만큼의 시간이 걸려 (절대시간)
            completeTime[conIdx] = endTime;                         // 그래서 기록할래.
            answer = Math.max(answer, endTime);

            // 이제 다 지었으니까.
            // 내가 앞선 노드인 경우..를 지워줘야 해. ~> 내가 앞선 노드.. 인걸 어떻게 알아?
            for(int afterIdx : adjList.get(conIdx)) {       // conIdx를 선행노드로 하는 후행 노드가 기록되어있어.
                priorLink[afterIdx]--;                      // 해당꺼를 감소시켜버린다 이거야.
                if(priorLink[afterIdx] == 0) {              // 비로소 0이 되어버렸으면
                    q.add(afterIdx);                            // 큐에 넣어버려라 앂새야.
                }
            }
        }

        for(int i =1; i<=N; i++ ) {
            System.out.println(completeTime[i]);
        }

    }
}







