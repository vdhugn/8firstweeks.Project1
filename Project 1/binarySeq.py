n = int(input()) + 1
x = [j for j in range(n)]

def solution(x):
    for i in range(1, n):
        print(str(x[i]), end = ' ')
    print()

def check(v, k):
    if v == 1 and x[k - 1] == 1:
        return 0
    else:
        return 1

def Try(k):
    for v in range(2):
        if check(v, k):
            x[k] = v
            if k == n - 1:
                solution(x)
            else:
                Try(k + 1)

Try(1)