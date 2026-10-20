def alfabetisch(zin):
    zin = zin.split()
    zin = sorted(zin)
    return zin


if __name__ == "__main__":
    zin = input()
    print(*alfabetisch(zin))

