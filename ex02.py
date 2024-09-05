caracteres = input("Digite uma palavra ou frase: ").strip().upper()
separar = caracteres.split()
juntar = "".join(separar)
contrario = juntar[::-1]

if juntar == contrario:
    print("A sequência de caracteres é palíndromo")
else:
    print("A sequência de caracteres não é palíndromo")
