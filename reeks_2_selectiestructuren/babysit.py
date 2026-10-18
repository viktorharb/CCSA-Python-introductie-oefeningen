def bereken_verdienst(start_uur, start_minuut, eind_uur, eind_minuut):
    start = start_uur * 60 + start_minuut
    eind = eind_uur * 60 + eind_minuut
    
    if start > eind: 
        return "ongeldige invoer"
    elif eind <= 1290:                    
        return (eind - start) / 60 * 2
    elif start >= 1290:                   
        return (eind - start) / 60 * 4
    else: 
        uren_aan_4_euro = (eind - 1290) / 60
        uren_aan_2_euro = (1290 - start) / 60
        return uren_aan_4_euro * 4 + uren_aan_2_euro * 2


uren = [int(input()) for _ in range(4)]
print(bereken_verdienst(*uren), sep="\n")