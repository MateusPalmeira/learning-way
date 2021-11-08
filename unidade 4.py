# def area_triangret(base, altura):
#     formula = (base*altura)/2
#     return formula

# base = int(input("Digite o valor da base do triangulo (em cms): "))
# altura = int(input("Digite o valor da altura do triangulo (em cms): "))
# area = area_triangret(base, altura)
# print("A area do triangulo é:{:.1f}cms".format(area))

## vê se o numero é positivo, negativo ou 0 ##
def verifica_valor(valor):
    if valor > 0:
        return 'o número {} é positivo!'.format(valor)
    if valor == 0:
        return 'o número {} é zero!'.format(valor)
    else:
        return 'o numero {} é negativo!'.format(valor)

val=int(input('digite um numero inteiro: '))
resultado = verifica_valor(valor=val)
print(resultado)
