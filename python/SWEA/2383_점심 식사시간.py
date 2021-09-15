from itertools import combinations
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    stair_pos = []
    people_pos = []
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(n):
            if data[j] == 1:
                people_pos.append([i, j])
            elif data[j] > 1:
                stair_pos.append([data[j], i, j])

    people_dist = []
    num_list = []
    for i in range(len(people_pos)):
        x, y = people_pos[i]
        num_list.append(i)
        people_dist.append([abs(x-stair_pos[0][1]) + abs(y-stair_pos[0][2]), abs(x-stair_pos[1][1]) + abs(y-stair_pos[1][2])])

    if len(people_dist) == 1:
        print('#' + str(test_case) + ' ' + str(min(people_dist[0][0] + stair_pos[0][0] + 1, people_dist[0][1] + stair_pos[1][0] + 1)))
        continue

    answer = 1e9
    for num in range(len(people_dist) + 1):
        num_select = list(combinations(num_list, num))

        for c in num_select:
            people_list1 = []
            people_list2 = []
            for idx in range(len(people_dist)):
                if idx in c:
                    people_list1.append(people_dist[idx][0])
                else:
                    people_list2.append(people_dist[idx][1])

            people_list1 = deque(sorted(people_list1))
            people_list2 = deque(sorted(people_list2))

            q1 = deque()
            q2 = deque()
            time = 0
            while True:
                if time >= answer or (not q1 and not q2 and not people_list1 and not people_list2):
                    break
                time += 1

                for i in range(min(3, len(q1))):
                    q1[i] -= 1
                while q1:
                    if q1[0] == 0:
                        q1.popleft()
                    else:
                        break
                for i in range(min(3, len(q2))):
                    q2[i] -= 1
                while q2:
                    if q2[0] == 0:
                        q2.popleft()
                    else:
                        break

                for i in range(len(people_list1)):
                    people_list1[i] -= 1
                for i in range(len(people_list2)):
                    people_list2[i] -= 1
                while people_list1:
                    if people_list1[0] == 0:
                        people_list1.popleft()
                        if len(q1) < 3:
                            q1.append(stair_pos[0][0]+1)
                        else:
                            q1.append(stair_pos[0][0])
                    else:
                        break
                while people_list2:
                    if people_list2[0] == 0:
                        people_list2.popleft()
                        if len(q2) < 3:
                            q2.append(stair_pos[1][0]+1)
                        else:
                            q2.append(stair_pos[1][0])
                    else:
                        break

            answer = min(time, answer)

    print('#' + str(test_case) + ' ' + str(answer))