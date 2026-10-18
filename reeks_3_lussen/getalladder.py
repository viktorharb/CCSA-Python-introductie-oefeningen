def maak_ladder(getal):
    for i in range(getal):
        for j in range(i + 1): 
            print(j + 1, end="")
        print()
getal = int(input())
maak_ladder(getal)