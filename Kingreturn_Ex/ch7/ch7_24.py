# break指令的應用
players = ['Curry', 'Jordan', 'dJames', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數 ＝ "))
if n > len(players):
    n = len(players)  # 列出人數不大於串列元素數
index = 0  # 索引
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1  # 索引加1