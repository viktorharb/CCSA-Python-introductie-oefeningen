def controleer_code(cijfers):
    return "OK" if sum([cijfers[i]*(i+1) for i in range(9)]) % 11 == cijfers[9]  else "FOUT" 


cijfers = [int(input() )for i in range(10)]
print(controleer_code(cijfers))
