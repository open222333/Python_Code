# 專題 蒙地卡羅模擬
import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * -1  # x軸座標
    y = random.random() * - 1  # y軸座標
    if x * x + y * y <= 1:  # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials
print("PI = ", PI)