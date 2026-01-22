import sys
from queue import PriorityQueue

input = sys.stdin.readline

q = PriorityQueue()

N = int(input())

for _ in range(N):
    card = int(input())
    q.put(card)

result = 0

while q.qsize() > 1:
    first_card = q.get()
    second_card = q.get()
    card_sum = first_card + second_card
    q.put(card_sum)

    result += card_sum

print(result)