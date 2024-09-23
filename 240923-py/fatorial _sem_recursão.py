#calculo do fatorial (sem recursão)

def fatorial(n):
    fat = 1
    for i in range (1, n+1):
        fat *= i
    return fat

#principal 
num = int(input('Número: '))
print(f'Faorial de {num}: {fatorial(num)}')