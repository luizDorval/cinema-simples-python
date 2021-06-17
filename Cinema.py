def menu_inicial():  # Menu Principal
    print("\n1 - Carregar dados")
    print("2 - Consultar situação de um assento")
    print("3 - Fazer reserva de 'n' assentos")
    print("4 - Liberar reserva de 'n' assentos")
    print("5 - Visualizar mapa do cinema")
    print("6 - Salvar dados")
    print("7 - Encerrar sessão do filme")
    escolha_menu_inicial = input("\nDigite a opção desejada: ")
    return escolha_menu_inicial


def info_ocupante(sexo, idade):  # Armazena as informações do ocupante na matriz
    sexo = input("Digite o sexo do ocupante: ")
    idade = int(input("Digite a idade do ocupante: "))
    # precisa resolver a questão da coluna pra armazenas no lugar certo kkkkkkkk
    for i in range(ocupantes):
        ocupantes.append(sexo, idade)


valor_ingresso = float(
    input("Informe o valor do ingresso: "))  # Valor do Ingresso
qntFileiras = int(input("Informe a quantidade de fileiras: ")
                  )  # Quantidade de Fileiras
# Quantidade de assentos
qntAssentos = int(input("Informe a quantidade de assentos por fileira: "))

ocupantes = []  # Matriz dados dos ocupantes
assentos = []  # Quantidade total de assentos
for i in range(qntFileiras):
    assentos.append([])
    for j in range(qntAssentos):
        assentos[i].append('"."')

escolha_menu_inicial = 0
while (escolha_menu_inicial != '7'):
    escolha_menu_inicial = menu_inicial()  # Entra na função menu, alterando o valor
    if (escolha_menu_inicial == '1'):
        print("Informa nome do arquivo que contém o registro das reservas")

    elif (escolha_menu_inicial == '2'):
        print("Informar assento e retorna se está liberado ou não")

    elif (escolha_menu_inicial == '3'):  # Reservar assento
        reservarAssentos = int(input("Quantos assentos deseja reservar? "))
        fileira = int(
            input("Qual a fileira em que deseja reservar os assentos? "))
        primeiro_assento = int(
            input("A partir de qual assento deseja fazer a reserva? "))
        for i in range(qntFileiras):
            print(i)
            if(i == fileira):
                k = primeiro_assento
                for j in range(reservarAssentos):
                    assentos[fileira][k] = '"X"'
                    k += 1
                    print(k, 'kkkk')
        print("Assentos reservados!")

    elif (escolha_menu_inicial == '4'):  # Liberar assento
        limparAssentos = int(input("Quantos assentos deseja liberar? "))
        fileira = int(
            input("Qual a fileira em que deseja liberar os assentos? "))
        primeiro_assento = int(
            input("A partir de qual assento deseja remover as reservas? "))
        for i in range(fileira):
            for j in range(limparAssentos):
                assentos[i][j] = "."
        print("Assentos liberados!")

    if (escolha_menu_inicial == '5'):
        # Mostrar mapa do cinema
        print(assentos[5][5])
        for i in range(qntAssentos):  # Apenas informa o número da coluna
            if(i == 0):
                print(' ', end="    ")
            i = i+1
            print(i, end="   ")
        print()
        for i in range(qntFileiras):
            print(chr(65+i), end=' ')  # Informa a coluna como uma letra
            print('[', end=" ")
            for j in range(qntAssentos):
                print(assentos[i][j], end=" ")
            print(']\n')

    if (escolha_menu_inicial == '6'):
        print("Informa nome do arquivo e salva as reservas")
