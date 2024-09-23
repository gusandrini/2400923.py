#calculo do fatorial (com recursão)

def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial(n-1)

#principal 
num = int(input('Número: '))
print(f'Faorial de {num}: {fatorial(num)}')