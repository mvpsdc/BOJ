a = [1,2,3,4,5]

def solve(a):
    result = 0

    for i in range(len(a)):
        result += a[i]

    return result

solve(a)
