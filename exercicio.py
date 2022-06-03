#! /usr/bin/env python3
__version__ = "0.1.0"

"""Encontrar os numeros primos"""

numero = int(input("Digite um numero inteiro: "))
print(f"O numero digitado e: {numero}")

if numero <= 0: 
    print("numero deve ser maior que 0")
    exit()

if (numero % 2) == 0: 
    print(f"O numero {numero} e par")
else: 
    print(f"O numero {numero} e impar")
