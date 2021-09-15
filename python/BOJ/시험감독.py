n = int(input())
data = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for d in data:
    people = d - b
    answer += 1
    if people > 0:
        answer += (people // c)
        people %= c
        if people > 0:
            answer += 1

print(answer)
