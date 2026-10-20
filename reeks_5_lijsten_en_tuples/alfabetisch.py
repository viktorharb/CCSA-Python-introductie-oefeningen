def alfabetisch(zin):
    woorden = sorted(zin.split())
    return " ".join(woorden)


if __name__ == "__main__":
    zin = input()
    print(alfabetisch(zin))

