import math as m
def bereken_vierkantsvergelijking(a, b, c):
    delta = b ** 2 - 4 * a * c 
    if delta == 0: 
        return "een wortel", (-b / (2 * a))
    elif delta > 0: 
        x1 = ((-b - m.sqrt(delta)) / (2 * a))
        x2 = ((-b + m.sqrt(delta)) / (2 * a))
        return "twee wortels", min(x1, x2), max(x1, x2)
    else: 
        return "geen wortels",

coefficienten = [float(input()) for i in range(3)]
print(*bereken_vierkantsvergelijking(*coefficienten), sep="\n")