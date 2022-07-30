import java.io.*;
import java.util.*;

public class Main {

    static int N = 0;
    static int[] numbers;
    static boolean[] check;

    public static void dfs(int depth, int start) {
        if(depth == 6) {
            for(int i=0; i<N; i++) {
                if(check[i]){
                    System.out.print(numbers[i] + " ");
                }
            }
            System.out.println();
        }

        System.out.println("depth = " + depth);
        System.out.println("start = " + start);
        for(int val : numbers) {
            System.out.print(val + " ");
        }
        for(boolean is : check) {
            System.out.print(is + " ");
        }
        Scanner sc = new Scanner(System.in);
        sc.nextInt();

        for(int i=start; i<N; i++) {
            check[i] = true;
            dfs(depth+1, i+1);
            check[i] = false;
        }
    }

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            if(N == 0) {
                break;
            }
            numbers = new int[N];
            check = new boolean[N];
            for(int i=0; i<N; i++) {
                numbers[i] = Integer.parseInt(st.nextToken());
            }
            dfs(0, 0);
            System.out.println();
        }
    }
}

