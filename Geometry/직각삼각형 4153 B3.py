import sys

input = sys.stdin.readline

while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")