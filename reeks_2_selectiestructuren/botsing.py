def check_botsing(x1, y1, x2, y2, x3, y3, x4, y4):
    return "botsing" if y3 < max(y1, y2) and y3 > min(y1, y2) and x3 < max(x1, x2) and x3 > min(x1,x2) and x1 != x3 and y1 != y3 or x4 < max(x1, x2) and x4 > min(x1,x2) and y4 < max(y1, y2) and y4 > min(y1, y2) and x2 != x4 and y2 != y4 else "geen botsing"



coordinaten = [int(input()) for _ in range(8)]
print(check_botsing(*coordinaten))