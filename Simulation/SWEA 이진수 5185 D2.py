T = int(input())

for test_case in range(1, T + 1):

    N, N_16 = input().split()
    
    N_16 = int(N_16, 16)    # 16진수 문자열을 정수로 변환 후 2진수로 변환
    N_2 = bin(N_16)[2:].zfill(4*int(N))  # '0b' 제거 후 4xN 길이만큼 0 채우기

    print(f"#{test_case} {N_2}")