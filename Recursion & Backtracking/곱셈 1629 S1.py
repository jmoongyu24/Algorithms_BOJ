A, B, C = map(int,input().split())

def mul(a, b, c):
    if b == 1:
        return a % c
    # b를 반으로 나눔으로써 곱셈 횟수를 줄임 4%3 이나 16%3이나 똑같음
    val = mul(a, b // 2, c)
    val = (val * val) % c

    if b % 2 == 0:
        return val
    
    return val * a % c

print(mul(A, B, C))