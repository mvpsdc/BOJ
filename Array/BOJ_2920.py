ar = list(map(int, input().split()))

ar_sorted = sorted(ar)
ar_reverse_sorted = list(reversed(ar_sorted))

if ar == ar_sorted:
    print('ascending')
elif ar == ar_reverse_sorted:
    print('desceding')
else: print('mixed')