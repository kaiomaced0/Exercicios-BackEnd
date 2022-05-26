'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas 
de tinta a serem compradas e o preço total.
'''
import math
tinta = 1
lataTinta = 18 * tinta
valorLata = 80

print("Infome a quantidade em Metros Quadrados a serem pintados")
quantM = (int(input()))
latas = (((quantM / 3) * tinta) / lataTinta)
latas = math.ceil(latas)
valorFinal = valorLata * latas
print (f'O valor final a ser pago é de R${valorFinal},00, ou seja, {latas} Latas de tinta.')
