def bovensteboven(getal):
    foute_getallen = "23457"
    return False if any(c in foute_getallen for c in getal) or getal[-1] == "0" else True
    volgende(getal)


def volgende(getal):
    return None

if __name__ == "__main__":
    getal = (input())
    print(bovensteboven(getal))
