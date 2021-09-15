# 2021.04.20 PM 4:43 ~
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    magnet = {}
    for i in range(4):
        magnet[i] = deque(list(map(int, input().split())))

    move = []
    for i in range(k):
        move.append(list(map(int, input().split())))

    for time in range(k):
        num, d = move[time]
        q = deque()
        q.append([num-1, d, 2])
        while q:
            num, d, check_d = q.popleft()
            if check_d == 0 or check_d == 2: #왼쪽확인
                new_num = num - 1
                if new_num >= 0 and magnet[new_num][2] != magnet[num][6]:
                    q.append([new_num, d * (-1), 0])

            if check_d == 1 or check_d == 2: #오른쪽확인
                new_num = num + 1
                if new_num <= 3 and magnet[new_num][6] != magnet[num][2]:
                    q.append([new_num, d * (-1), 1])

            if d == 1: # 시계방향
                x = magnet[num].pop()
                magnet[num].appendleft(x)
            else:
                x = magnet[num].popleft()
                magnet[num].append(x)

    answer = 0
    for num in range(4):
        if magnet[num][0] == 1:
            answer += 2 ** num

    print('#'+str(test_case)+' '+str(answer))