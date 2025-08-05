board=input()

# board에서 XXXX를 앞에서부터 순서대로 치환
board = board.replace("XXXX", "AAAA")

# board에서 XXXX를 치환하고 남은 XX를 앞에서부터 순서대로 치환
board = board.replace("XX", "BB")

# X로 치환했는데도 남아있다면 -1 출력
if 'X' in board:
    print(-1)

else:
    print(board)