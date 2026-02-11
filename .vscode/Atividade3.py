contador = 1
soma_nota = 0
while contador <= 4:
    nota = float(input(f"Insira a nota do {contador} aluno"))
    soma_notas += nota 
    contador +=1 
media = soma_notas/4
print("A media das quatro notas é: ",media)