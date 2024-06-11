#input
# email = input("Escreva seu e-mail: ")
# nome = input("Seu primeiro nome:")

# print(nome,email)

#faturamento = float(input("Escreva o faturamento: "))
# sempre precisamos definir o que a váriavel é, nesse caso acima é float
 
# print(f"{nome}, verifique seu email {email} que enviamos um link de confirmação!")

#imposto = faturamento * 0.1


#listas

vendas = [100,50,14,20,30,700]

#soma dos elementos 

total_vendas = sum(vendas)

#tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

#max e min
print(max(vendas))
print(min(vendas))

#pegar posições
print(vendas[5]) 


lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

# produto_procurado = input("Pesquise pelo nome do produto: ")

# armazenamos a pesquisa dentro de uma variável, colocamos ela em letra minuscula
# produto_procurado = produto_procurado.lower()

# # colocando o elemento em letra minusculo, deixamos da mesma forma que está armazenado dentro da lista para que a procura abaixo diga se é verdadeiro ou falso
# print(produto_procurado in lista_produtos)


# adicionar im item
lista_produtos.append("apple watch")

#remover um item
lista_produtos.remove("apple watch")
# dessa maneira ele remove pelo nome, mas podemos remover pela posição que é o pop
lista_produtos.pop(0)
# remove o elemento da primeira posição

#editar um item
precos = [1000, 1500, 3500]
precos[0] = precos[0] * 1.5

lista_produtos = ["iphone", "airpod", "ipad", "macbook","iphone", "airpod"]

# conta quantas vezes a palavra iphone aparece na lista
print(lista_produtos.count("iphone"))

# ordenar

lista_produtos.sort(reverse=False)
print(lista_produtos)