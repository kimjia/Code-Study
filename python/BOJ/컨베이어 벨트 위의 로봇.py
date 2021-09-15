from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)

score = 0
time = 0
while score < k:

    # 1. 컨베이어 벨트 한 칸 회전
    x = belt.pop()
    belt.appendleft(x)
    y = robot.pop()
    robot.appendleft(0)

    # 2. 이동할 수 있는 로봇 이동
    if robot[n-1]:
        robot[n-1] = 0
    for i in range(n-2, 0, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                score += 1

    # 3. 올라갈 위치에 로봇 없으면 올리기
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            score += 1

    time += 1

print(time)