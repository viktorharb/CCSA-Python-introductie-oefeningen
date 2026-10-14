def bereken_fahrenheit(tjirps):
    return 50 + (tjirps - 40) / 4


def bereken_celsius(tjirps):
    return 10 + (tjirps - 40) / 7


n = int(input())
print(f"temperatuur (Fahrenheit): {bereken_fahrenheit(n)}")
print(f"temperatuur (Celsius): {bereken_celsius(n)}")