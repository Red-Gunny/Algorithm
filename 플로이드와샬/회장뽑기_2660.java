import java.io.*;
import java.util.*;

public class Main {

    static int memberCnt = 0;
    static int[][] adjArr;
    static int result = 987654321;
    static List<Integer> q;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        memberCnt = Integer.parseInt(br.readLine());
        adjArr = new int[memberCnt+1][memberCnt+1];
        for(int i=0; i<=memberCnt; i++) {
            for(int j=0; j<=memberCnt; j++) {
                adjArr[i][j] = 10000;
            }
        }
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int user1 = Integer.parseInt(st.nextToken());
            int user2 = Integer.parseInt(st.nextToken());
            if(user1 == -1 && user2 == -1) {
                break;
            }
            adjArr[user1][user2] = adjArr[user2][user1] = 1;
        }

        for(int k=1; k<=memberCnt; k++) {
            for(int i=1; i<=memberCnt; i++) {
                for(int j=1; j<=memberCnt; j++) {
                    adjArr[i][j] = Math.min(adjArr[i][j], adjArr[i][k] + adjArr[k][j]);
                    if(i == j) {
                        adjArr[i][j] = 0;
                    }
                }
            }
        }

        q = new ArrayList<>(51);
        for(int i=1; i<=memberCnt; i++) {
            int maxCnt = 0;
            for(int j=1; j<=memberCnt; j++) {
                maxCnt = Math.max(maxCnt, adjArr[i][j]);
            }
            if(result > maxCnt) {      // result 가 바뀌어야함 -> 큐 초기화
                result = maxCnt;
                q.clear();
                q.add(i);
            }
            else if (result == maxCnt){
                q.add(i);
            }
        }

        System.out.println(result + " " + q.size());
        for(var data : q) {
            System.out.print(data + " ");
        }
    }


}

/*for(int i=1; i<=memberCnt; i++) {
            for(int j=1; j<=memberCnt; j++) {
                System.out.print(adjArr[i][j] + " ");
            }
            System.out.println();
        }*/
