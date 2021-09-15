# 2021.04.15 PM 10:02~10:34
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    data = deque(list(input()))

    length = n // 4
    num_list = []
    for i in range(length):
        for number in range(4):
            result = 0
            start = number * length
            for idx in range(length):
                letter = data[start + idx]
                if letter == 'A':
                    letter = 10
                elif letter == 'B':
                    letter = 11
                elif letter == 'C':
                    letter = 12
                elif letter == 'D':
                    letter = 13
                elif letter == 'E':
                    letter = 14
                elif letter == 'F':
                    letter = 15
                else:
                    letter = int(letter)

                result = result * 16 + letter
                # print(result, letter)
            if result not in num_list:
                num_list.append(result)
        x = data.pop()
        data.appendleft(x)

    num_list.sort(reverse=True)
    print('#' + str(test_case))
    print(num_list[k-1])


