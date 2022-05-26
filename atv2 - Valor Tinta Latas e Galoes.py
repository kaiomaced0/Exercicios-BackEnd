'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
preços em 3 situações: 
    -comprar apenas latas de 18 litros;
    -comprar apenas galões de 3,6 litros;
    -misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
    e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
from asyncore import compact_traceback
import math;
quantM = (int(input("Informe o tamanho a ser pintado em Metros quadrados:")))
quantM = (quantM * 1.1)
precoLata = 80.0
precoGalao = 25.0
lataT = 18
galaoT = 3.6
latasCompradas = quantM / lataT
quantidadeFaltante = latasCompradas
soLatas = math.ceil(latasCompradas)
latasCompradas = math.floor(latasCompradas)
galaoComprados = math.ceil(quantM / galaoT)
quantidadeFaltante = (quantidadeFaltante - latasCompradas) * lataT
galaoTest = 0
while quantidadeFaltante > 0 :
    galaoTest = 1 + galaoTest
    quantidadeFaltante = quantidadeFaltante - galaoT

compraLataFinal = (int(soLatas * precoLata))
compraGalaoFinal = (int(galaoComprados * precoGalao))
compraFinal = (int((precoLata * latasCompradas) + (precoGalao * galaoTest)))
print(f'Na compra de apenas Latas, serão consumidas {soLatas} -Latas e o valor fica em R${compraLataFinal},00')
print(f'Na compra de apenas Galões, serão consumidos {galaoComprados} -Latas e o valor fica em R${compraGalaoFinal},00')
print(f"Foram utilizadas Latas - {latasCompradas} e Galões - {galaoTest}. Dando um total de R${compraFinal},00")
