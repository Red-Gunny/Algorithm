import java.io.*;
import java.util.*;

public class Main {

    static int N = 0;
    static ArrayList<Node> tree;

    static class Node {
        int parent = -1;
        int me;
        List<Integer> child;
        Node(int me) {
            this.me = me;
            child = new LinkedList<>();
        }
    }

    static int deleteNode = 0;

    static int rootNum = 0;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());    // 트리의 개수
        StringTokenizer st = new StringTokenizer(br.readLine());
        tree = new ArrayList<>();
        for(int i=0; i<N; i++) {
            tree.add(new Node(i));      // 일단 맨들어놔.
        }

        for(int i =0; i<N; i++) {
            int parent = Integer.parseInt(st.nextToken());      // 이게 현재 인덱스의 부모 번호래.
            if(parent == -1) {      // 부모가 없으면 무시데스
                rootNum = i;
                continue;
            }
            Node curNode = tree.get(i);         // 현재 노드
            curNode.parent = parent;            // 현재 노드의 부모 설정
            Node parentNode = tree.get(parent); // 부모 가져옴
            parentNode.child.add(i);
        }

        deleteNode = Integer.parseInt(br.readLine());
        if(deleteNode == rootNum) {
            System.out.println(0);
            return;
        }
        deleteRoot(deleteNode);
        int cnt = getLeafNodeCnt(tree.get(rootNum));
        System.out.println(cnt);
    }

    public static int getLeafNodeCnt(Node node) {
        int sum=0;
        if(node.child.size() == 0) {        // 자식 노드 번호가 둘다 -1 이면 리턴 1
            return 1;
        }

        for(var data : node.child) {
            sum += getLeafNodeCnt(tree.get(data));
        }
        return sum;
    }

    public static void deleteRoot(int idx) {
        Node node = tree.get(idx);         // 지우려는 노드를 가져왐
        Node parentNode = tree.get(node.parent);        // 부모의 노드로..

        for(int i=0; i< parentNode.child.size(); i++) {
            if(parentNode.child.get(i) == idx) {
                parentNode.child.remove(i);
                break;
            }
        }
    }

}
