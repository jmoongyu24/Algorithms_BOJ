import sys

input=sys.stdin.readline

n=int(input())
rope=[]

for _ in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

result=0

for i in range(len(rope)):
    result=max(result, (i+1)*rope[i])

print(result)