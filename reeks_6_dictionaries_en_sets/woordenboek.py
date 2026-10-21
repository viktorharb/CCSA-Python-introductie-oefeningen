def vertaling_toevoegen(woord,vertaling,woordenboek):
    woordenboek[woord] = vertaling

def vertaling(woord,woordenboek):
    return woordenboek.get(woord, "???")


if __name__ == "__main__":
    woordenboek = {}
    vertaling_toevoegen('plerzs', 'vrouw', woordenboek)
    vertaling_toevoegen('tilza', 'hond', woordenboek)
    print(vertaling('tilza', woordenboek))
    print(vertaling('guoles', woordenboek))
