def maximale_blootstelling(decibel):
    GRENS_WAARDE = 80
    verschil = decibel - GRENS_WAARDE
    return -1 if verschil < 0 else (8 / (2 ** (verschil // 3)))


decibel = int(input())
print(maximale_blootstelling(decibel))
