import copy


key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
N, M = len(lock), len(key)

def solution(key, lock):
    answer=0
    appended_graph = append_up_and_down(lock)
    appended_graph = append_left_and_right(appended_graph)
    ro_key = copy.deepcopy(key)
    for _ in range(4):
        ro_key = rotate(ro_key)     # 키를 회전했어..
        answer = is_success(ro_key, appended_graph)
        if answer:
            break
    return answer

def is_success(key, lock):
    for i in range(N-M+1):
        answer_cnt = 0
        for j in range(M):
            for k in range(M):
                # print(i+j, end=' & ')
                # print(i+k)
                if lock[i+j][i+k] == -1:
                    answer_cnt += 1
                    continue
                if lock[i+j][i+k] + key[j][k] == 1:
                    answer_cnt += 1
                else:
                    break
        # print("========================================")
        # print(answer_cnt)
        # print("========================================")
        if answer_cnt == M*M:
            return True
    return False


def rotate(graph):
    copied = copy.deepcopy(graph)
    for b in range(M-1, -1, -1):      # key의 가로 개수 만큼 거꾸로 바놉
        for a in range(M):     # key의 원소 개수만큼 반복
            graph[a][b] = copied[(M-1)-b][a]   # 3-2
    return copy.deepcopy(graph)

def append_up_and_down(graph):      # lock이 들어온다.
    tmp = [-1]*len(graph[0])
    for i in range(M-1):
        temp = copy.deepcopy(tmp)
        graph.insert(0, temp)
        temp2 = copy.deepcopy(tmp)
        graph.append(temp2)
    return copy.deepcopy(graph)

def append_left_and_right(graph):
    lock_size = len(graph)
    for i in range(lock_size):      # lock 사이즈만큼 반복... (가로 개수)
        for j in range(M-1):        # 늘려야 하는 사이즈 만큼 반복. (M-1)
            graph[i].insert(0, -1)
            graph[i].append(-1)
    return graph


print(solution(key, lock))