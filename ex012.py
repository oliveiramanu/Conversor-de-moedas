preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print("o produto que custava R${} na promoção com desconto de 5% vai valer R${}".format(preco, novo))
