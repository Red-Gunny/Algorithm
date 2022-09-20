import math
from collections import deque
fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

d_time, d_cost, u_time, u_cost = 0, 0, 0, 0
in_map = {}
parking_time_map = {}
result_map = {}

def solution():
    global d_time, d_cost, u_time, u_cost
    d_time, d_cost, u_time, u_cost = fees
    q_records = deque(records)
    for data in records:
        car_inout = data.split()
        if car_inout[2] == "IN":    # 입력 기록
            car_num = int(car_inout[1])
            in_map[car_num] = car_inout[0]
        elif car_inout[2] == "OUT":     # 출력
            car_num = int(car_inout[1])
            in_time = in_map[car_num]       # 입력 시각
            del(in_map[car_num])
            out_time = car_inout[0]         # 나간 시각
            diff_time = get_diff_by_minute(in_time, out_time)       # 시간 차이를 구함 (분 단위)
            if car_num not in parking_time_map:     # 주차 아다면
                parking_time_map[car_num] = diff_time
            else:                                   # 주차 후다면
                parking_time_map[car_num] += diff_time
    for remain in in_map:
        in_time = in_map[remain]
        out_time = "23:59"
        diff_time = get_diff_by_minute(in_time, out_time)
        if remain not in parking_time_map:  # 주차 아다면
            parking_time_map[remain] = diff_time
        else:  # 주차 후다면
            parking_time_map[remain] += diff_time

    for number in parking_time_map:
        diff_time = parking_time_map[number]        # 주차장에 있던 시간
        car_cost = get_cost(diff_time)              # 비용 계산
        if number in result_map:
            result_map[number] += car_cost
        else:
            result_map[number] = car_cost  # 없으면
    sorted_result = sorted(result_map.items(), key=lambda x: x[0])
    result = []
    for a, b in sorted_result:
        result.append(b)
    return result

def get_cost(time):
    global d_time, d_cost, u_time, u_cost
    if time <= d_time:
        return d_cost
    return math.ceil((time - d_time)/u_time) * u_cost + d_cost


def get_diff_by_minute(in_time, out_time):
    in_whole_min = get_whole_time(in_time)
    out_whole_min = get_whole_time(out_time)
    return out_whole_min - in_whole_min


def get_whole_time(time):
    hour_and_min = time.split(':')
    return int(hour_and_min[0])*60 + int(hour_and_min[1])

print(solution())



'''
print(car_num, end="의 시간.. ")
print(diff_time)

print(car_num, end="의 비용.. ")
print(car_cost)
'''