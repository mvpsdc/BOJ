N = int(input())

def hansu(n):
    if n <= 99:
        return n
    elif n <= 110:
        return 99
    else:
        nhansu = 0
        for i in range(111, n+1):
            a = i // 100
            b = (i // 10) % 10
            c = i % 10

            if (a - b) == (b - c):
                nhansu += 1
        return 99 + nhansu

print(hansu(N))