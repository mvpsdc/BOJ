len, x = map(int, input().split())
ar = list(map(int, input().split()))

result = []

for i in range(len):
    if ar[i] < x:
        result.append(ar[i])

for j in result:
    print(j, end = ' ')