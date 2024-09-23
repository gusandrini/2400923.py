#calcular a soma de uma lista de números (sem recursão)
#[1, 3, 5, 7, 9]

def soma_numeros(lista):
    soma = 0
    for i in lista:
        soma += i 
    return soma

#principal 
lista = [ 1, 3, 5, 7, 9]
print(f'{soma_numeros(lista)}')