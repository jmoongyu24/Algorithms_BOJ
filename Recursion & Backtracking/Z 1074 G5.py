N, R, C = map(int, input().split())

def Z(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)

    if r < half and c <half:    # r,c의 위치가 1사분면일 때
        return Z(n-1, r, c)
    
    if r < half and c >= half:  # r,c의 위치가 2사분면일 때
        return half * half + Z(n - 1, r, c - half)
    
    if r >= half and c < half:  # r,c의 위치가 3사분면일 때
        return 2 * half * half + Z(n - 1, r - half, c)
    
    return 3 * half * half + Z(n-1, r-half, c-half) # r,c의 위치가 4사분면일 때

print(Z(N, R, C))