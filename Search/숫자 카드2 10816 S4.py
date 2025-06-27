n=int(input())
card=list(map(int, input().split()))

# 상근이가 갖고 있는 카드의 개수를 딕셔너리 dict1에 저장, O(N)
dict1={}
for num in card:
    if num in dict1:
        dict1[num]+=1
    else:
        dict1[num]=1

# 찾을 숫자 목록을 find 리스트에 저장
m=int(input())
find=list(map(int, input().split()))

# 딕셔너리에서 찾을 숫자들의 개수를 출력, O(N)
answer=[]
for num in find:
    if num in dict1:
        answer.append(str(dict1[num]))
    else:
        answer.append("0")

print(" ".join(answer))