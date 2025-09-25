s = input()
a_cnt = s.count('a')
result = 99999

# 원형이므로 처음부터 a_cnt-1개 만큼 더 붙여줌 / 예를 들어 aabaa -> aabaa + aab,
# aaba, abaa, baaa, aaaa 이렇게 a의 갯수만큼 슬라이딩 윈도우로 탐색해야 함. 
# 이렇게 만들어진 윈도우 중, #b를 a로 바꾸는 횟수가 최소인 경우가 답
s += s[0:a_cnt-1]

for i in range(len(s)-(a_cnt-1)):
    result = min(result, s[i:i+a_cnt].count('b'))
print(result)
"""
이렇게 하나하나 비교하는 방식으로 접근하는 것이 아님
a_cnt = 0
result = 0

for i in range(len(s)-1):
    if i==0:
        if s[i] == 'a' and s[-1] == 'a' and s[i+1] == 'a':
            continue
        if s[i] == ' a' and s[-1] == 'a' and s[i+1] == 'b':
            continue
        if s[i] == 'a' and s[-1] == 'b' and s[i+1] == 'b':
            result += 1
    else:
        if s[i] == 'a' and s[i+1] == 'b':
            a_cnt +=1
        if s[i] == 'b' and s[i+1] == 'b':
            continue
        if s[i] == 'b':
            if a_cnt >=2:
                a_cnt = 0
            else:
                a_cnt = 0
                result += 1
"""