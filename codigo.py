meu_nome = "paula"
minha_idade = 17

# duas formas de fazer o format mesclando texto com variável
print("Meu nome é {} e minha idade é {}".format(meu_nome, minha_idade))
print(f"Meu nome é {meu_nome} e minha idade é {minha_idade}")

meu_nome = meu_nome.upper()

# upper transforma o nome em letra maiucula e lower em minuscula

print(meu_nome)

email_paula = "paulamalisiamoreira@gmail.com"

print(email_paula.find("@"))
#  esse comando encontra a posicao do caractere, lembrando que começa no 0, e caso nao encontre, ele dita -1

print(len(email_paula))
# dita o tamanho do texto

print(email_paula[19])
# dita o elemento que está na posição 19

email_paula = email_paula.replace("gmail.com", "hotmail.com")
# substitui uma parte do texto, so nao sei em que caso usariamos isso??

nome_aleatorio = "paula malisia"

print(nome_aleatorio.capitalize())
# capitaliza a primeira letra
print(nome_aleatorio.title())
# capitaliza a primera letra de cada palavra

salario = 176.99

print(f"Meu nome é {meu_nome} e meu salario é {salario:.1f}")

