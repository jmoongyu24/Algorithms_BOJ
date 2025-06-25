name=input()
name=''.join(sorted(name))  # 알파벳 순으로 정렬

dic={}  # 알파벳을 저장할 딕셔너리

for char in name:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1

# 홀수개인 알파벳이 2개 이상이면 팰린드롬 불가, odd_cnt로 홀수인 알파벳 개수 확인
odd_cnt=0
for k in dic:
    if dic[k]%2==0:
        continue
    else:
        odd_cnt+=1

# 홀수개인 알파벳이 2개 이상이면 불가
if odd_cnt>1:
    print("I'm Sorry Hansoo")

# 홀수개인 알파벳이 1개
else:
    result=""
    center=""           # 가운데에 들어갈 문자 저장
    for k in dic:
        if dic[k]%2==1:
            center=k

    half=""             # 앞의 절반이 될 문자열 만들기
    for k in dic:
        half=half+k*(dic[k]//2)
        
    for char in half:
        result=char+result

    result=half+center+result   # 앞 절반 + 가운데 문자 + 앞 절반의 역순

    print(result)