def ontleding(akkoord):
    if akkoord[1:2] != "#":
        return (akkoord[:1] , akkoord[1:])
    else:
        return (akkoord[:2], akkoord[2:])
    
def noten(grondnoot, toonintervallen):
    return 

print(ontleding('F'))
print(ontleding('Gm7'))
print(ontleding('D#M7'))