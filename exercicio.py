"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Heloisa Lima de Oliveira
2 - júlia Vitória dos Santos Azevedo Jesus

"""

import os
os.system("cls || clear")

def adicionando_familia(dados):
    salario = float(input("Digite o salário da família: "))
    filhos = int(input("Digite o número de filhos da família: "))
    dados.append((salario, filhos))
    salvar_dados(dados)
   

def exibir_resultados(dados):
    if not dados:
        print("Nenhuma família cadastrada.")
        return
    
    salarios = [s[0] for s in dados]
    media_salario = sum(salarios) / len(salarios)
    media_filhos = sum(s[1] for s in dados) / len(dados)

    print(f"Número de famílias: {len(dados)}")
    print(f"Média do salário: {media_salario:.2f}")
    print(f"Média de filhos: {media_filhos:.2f}")
    print(f"Maior salário: {max(salarios):.2f}")
    print(f"Menor salário: {min(salarios):.2f}")

def salvar_dados(dados):
    with open("pesquisa_prefeitura.txt", "w") as file:
        for salario, filhos in dados:
            file.write(f"{salario},{filhos}\n")

def ler_dados():
    if os.path.exists("pesquisa_prefeitura.txt"):
        with open("pesquisa_prefeitura.txt", "r") as file:
            return [tuple(map(float, line.strip().split(','))) for line in file]
    return []


dados = ler_dados()

while True:
    print("\nMenu:")
    print("1 - Adicionar família")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionando_familia(dados)
    elif escolha == '2':
        exibir_resultados(dados)
    elif escolha == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
