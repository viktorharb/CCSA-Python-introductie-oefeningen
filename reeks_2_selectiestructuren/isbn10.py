def controleer_code(cijfers):
    return "OK" if sum([cijfers[i]*(i+1) for i in range(10)]) % 11 <10 else "FOUT" 



cijfers = [int(input() )for i in range(10)]
print(controleer_code(cijfers))
