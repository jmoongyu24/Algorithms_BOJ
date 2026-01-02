exps = input().split('-') #'-'를 기준으로 split해서 exps 리스트에 저장

sum_list = [] #'-'로 나눈 항들의 합을 저장할 리스트

for exp in exps:
    sum = 0
    nums = exp.split('+') #덧셈을 하기 위해서 '+'를 기준으로 split
    
    for num in nums: #split한 리스트의 각 요소들을 더해줌
        sum += int(num)
    
    sum_list.append(sum) #각 항의 연산 결과(덧셈)를 sum_list에 저장

n = sum_list[0] #식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

for i in range(1,len(sum_list)): #1번째 값부터 n에서 빼준다
    n -= sum_list[i]
print(n)