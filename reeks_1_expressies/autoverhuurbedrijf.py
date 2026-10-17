
def bereken_benzineverbruik(b,e , l):
    return (l / (e - b)) * 100


b = float(input()) #kilomterteller begin
e = float(input()) #kilometer eind
l = float(input()) #liter benzinze te tanken

print(bereken_benzineverbruik(b, e, l))