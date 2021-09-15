from itertools import permutations
n = int(input())
data = list(map(int, input().split()))
operator = list(map(int, input().split()))  # add, sub, mul, div
op = []
for i, num in enumerate(operator):
    for _ in range(num):
        op.append(i)

permutation = set(permutations(op, n-1))

min_value = 1e9
max_value = -1e9


def calculate(a, b, op):  # 연산자에 맞는 계산 수행
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a/b)


for candidate in permutation:
    result = data[0]
    for i in range(n-1):
        result = calculate(result, data[i+1], candidate[i])
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
