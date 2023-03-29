real: float = float(input('Que valor tens na carteira? R$ '))

# cotação atual 1 dolar = 5.16

dolar = real / 5.16
euro = real / 5.61
libra = real / 6.37
iene = real / 0.039

print('Você possui em mãos o valor de R$ {} onde pode comprar {:.2f} em doláres'.format(real, dolar))
print('Você possui em mãos o valor de R$ {} onde pode comprar {:.2f} em euros'.format(real, euro))
print('Você possui em mãos o valor de R$ {} onde pode comprar {:.2f} em libras'.format(real, libra))
print('Você possui em mãos o valor de R$ {} onde pode comprar {:.2f} em ienes japôneses'.format(real, iene))
print('\n')
print("Espero que tenhamos ajudado :) ")
