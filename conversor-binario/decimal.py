while True:
    decimal = 0
    binario = str(input('Digite um número em binario: '))
    cont = len(binario)
    for i in binario:
        if i == '1':
            decimal += 2 ** (cont - 1)
        cont -= 1
    print(decimal)
