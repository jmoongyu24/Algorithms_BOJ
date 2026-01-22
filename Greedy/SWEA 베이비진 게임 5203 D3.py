T = int(input())

def check_winner(count):
        # Triplet
        for num in range(10):
            if count[num] >= 3:
                return True
        # Run
        for i in range(8):
            if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
                return True
        return False

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    
    count1 = [0] * 10  # 플레이어 1 카드 빈도
    count2 = [0] * 10  # 플레이어 2 카드 빈도


    is_win = False
    
    for i in range(len(nums)):    
        if i % 2 == 0:  # 플레이어 1
            count1[nums[i]] += 1
            if check_winner(count1):
                print(f"#{test_case} 1")
                is_win = True
                break
        else:  # 플레이어 2
            count2[nums[i]] += 1
            if check_winner(count2):
                print(f"#{test_case} 2")
                is_win = True
                break

    if not is_win:
        print(f"#{test_case} 0")