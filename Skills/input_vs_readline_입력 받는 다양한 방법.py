"""
맨 첫줄 Test case를 입력받을 때는 input() 사용해도 무방
그러나 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과 발생하지 않음
"""

# 참고: readline()은 프롬프트 메시지를 인수로 받을 수 없음
# x = sys.stdin.readline("입력하세요: ") # 에러
x = sys.stdin.readline()
print("입력하세요:", x)

import sys

# 1. 1개의 정수를 입력받을 때
# input()은 개행문자를 제거함, 개행문자만 없애서 줄바꿈없이 출력해 느림
# readline()은 개행문자를 제거하지 않음(=rstrip() 함수 적용 X)
# -> 형변환으로 '\n'을 제거해줘야 함
a = int(sys.stdin.readline())

# 2. 정해진 개수의 정수를 한줄에 입력받을 때
a,b,c = map(int,sys.stdin.readline().split())

# 3. 임의의 개수의 정수를 한줄에 받아 리스트에 저장할 때
data = list(map(int,sys.stdin.readline().split()))

# 4. 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
data = []
n = int(sys.stdin.readline())
for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

# 5. 문자열 n줄을 입력받아 리스트에 저장할 때
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]