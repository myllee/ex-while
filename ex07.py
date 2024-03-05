#7- Tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, 
#mostre qual é o maior valor existente na matriz desconsiderando os elementos da diagonal principal.

i = True
maior = 0

while i :
    numero = int (input("digite um numero inteiro e positivo ou 0 para terminar"))
    if numero > maior :
        maior = numero
    if numero == 0 :
        i = False
print(f"o maior numero digitado foi : {maior}")