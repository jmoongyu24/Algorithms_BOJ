from collections import deque

T = int(input())

for _ in range(T):
    q = deque()
    st = input()
    ok = True

    for ch in st:
        if ch =='(':
            q.append(ch)
        elif ch == ')' and len(q) > 0:
            q.popleft()
        elif ch == ')' and len(q) == 0:
            ok = False
            break
        
    if len(q) == 0 and ok == True:
        print("YES")
    else:
        print("NO")