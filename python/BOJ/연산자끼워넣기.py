n = int(input())
data = list(map(int, input().split()))
operator = list(map(int, input().split()))  # add, sub, mul, div


def calculate(a, b, op):  # 연산자에 맞는 계산 수행
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a/b)


min_value = 1e9
max_value = -1e9


def dfs(i, result):  # dfs로 모든 경우의 수 계산
    global min_value, max_value, operator
    if i == n:
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return -1

    for k in range(4):
        if operator[k] > 0:
            operator[k] -= 1
            dfs(i+1, calculate(result, data[i], k))
            operator[k] += 1


dfs(1, data[0])

print(max_value)
print(min_value)