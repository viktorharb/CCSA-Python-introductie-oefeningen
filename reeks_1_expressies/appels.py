CAPACITEIT_KIST = 20
CAPACITEIT_PALLET = 35

def vullen(appels):
    appels_per_pallet = CAPACITEIT_KIST * CAPACITEIT_PALLET
    gevulde_palleten = appels // appels_per_pallet
    rest = appels % appels_per_pallet
    kisten = rest // CAPACITEIT_KIST
    overschot = appels % CAPACITEIT_KIST

    return gevulde_palleten, kisten, overschot

appels = int(input())
print(*vullen(appels), sep="\n")