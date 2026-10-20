def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# def fib(getal):
#     fibo = [0, 1]

#     for _ in range(getal - 1):
#         fibo.append(fibo[-2] + fibo[-1])

#     print(fibo[getal])

if __name__ == "__main__":
    getal = int(input())
    fib(getal)