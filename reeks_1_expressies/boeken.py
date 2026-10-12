boek_prijs = 24.95
verzendingskosten = 0
KORTING = 0.4
VERSTUURSKOSTEN_EERSTE_BOEK = 3
VERSTUURSKOSTEN_TWEEDE_BOEK_EN_VOLGEND = 0.75

def berekenPrijs(aantal_boeken):
        verzendingskosten = (aantal_boeken - 1) * VERSTUURSKOSTEN_TWEEDE_BOEK_EN_VOLGEND + VERSTUURSKOSTEN_EERSTE_BOEK 
        prijs = (boek_prijs*aantal_boeken) * (1- KORTING) + verzendingskosten
        print (f"{prijs}")
berekenPrijs(60)


