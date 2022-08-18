from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    key_singo_member = defaultdict()
    key_is_singoed = defaultdict()

    for line in report:
        caller, callee = line.split(' ')
        if caller not in key_singo_member:
            key_singo_member[caller] = []
        if callee not in set(key_singo_member[caller]):
            key_singo_member[caller].append(callee)
        if callee not in key_is_singoed:
            key_is_singoed[callee] = []
        if caller not in set(key_is_singoed[callee]):
            key_is_singoed[callee].append(caller)

    for idx, id in enumerate(id_list):
        if id not in key_singo_member:
            continue
        for who in key_singo_member[id]:
            if who not in key_is_singoed:
                continue
            if len(key_is_singoed[who]) >= k:
                answer[idx] += 1

    return answer

