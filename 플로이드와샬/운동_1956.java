import java.io.*;
import java.util.*;

public class Main {

    static int V, E;
    static int[][] adjArr;

    static long answer = 987654321;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        adjArr = new int[V+1][V+1];
        for(int i=0; i<=V; i++) {
            for(int j=0; j<=V; j++) {
                adjArr[i][j] = 987654321;     //                adjArr[i][j] = 1000000;     //
            }
        }

        for(int i =0; i<E; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            adjArr[start][end] = cost;
        }


        for(int k=1; k<=V; k++) {
            for(int i=1; i<=V; i++) {
                for(int j=1; j<=V; j++) {
                    if(i==k || j==k) {        // 무의미한 계산은 스킵
                        continue;
                    }
                    if(i == j) {          // 자기 자신에 대한...
                        if(adjArr[i][k] + adjArr[k][j] != 0) {
                            answer = Math.min(answer, adjArr[i][k] + adjArr[k][j]);
                        }
                    }
                    adjArr[i][j] = Math.min(adjArr[i][j], adjArr[i][k] + adjArr[k][j]);
                }
            }
        }

        if(answer == 987654321) {
            System.out.println(-1);
        }else {
            System.out.println(answer);
        }
    }


}


/*adjArr[i][j] = adjArr[i][j] == 0 ?
                                adjArr[i][k] + adjArr[k][j] :
                                Math.min(adjArr[i][j], adjArr[i][k] + adjArr[k][j]);*/

        /*answer = 10000;
        for(int i =1; i<=V; i++) {
            answer = Math.min(answer, adjArr[i][i]);
        }*/

        /*for(int i=1; i<=V; i++) {
            for(int j=1; j<=V; j++) {
                System.out.print(adjArr[i][j] + " ");
            }
            System.out.println();
        }*/
