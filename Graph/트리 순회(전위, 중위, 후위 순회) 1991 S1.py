import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

lc = [0] * 30
rc = [0] * 30

for _ in range(N):
    cur, left_child, right_child = map(str, input().split())

    # A, B, C...의 알파벳 입력을 정수 0,1,2...로 변환
    # ord(): 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수 반환하는 함수
    if left_child != '.':
        lc[ord(cur) - ord('A') + 1] = ord(left_child) - ord('A') + 1
    if right_child != '.':
        rc[ord(cur) - ord('A') + 1] = ord(right_child) - ord('A') + 1

def preorder(cur):
    if cur == 0:
        return
    print(chr(cur + ord('A') - 1), end='')
    preorder(lc[cur])
    preorder(rc[cur])

def inorder(cur):
    if cur == 0:
        return
    inorder(lc[cur])
    print(chr(cur + ord('A') - 1), end='')
    inorder(rc[cur])

def postorder(cur):
    if cur == 0:
        return
    postorder(lc[cur])
    postorder(rc[cur])
    print(chr(cur + ord('A') - 1), end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)