#--- Limpeza de Historico para evitar o acumulo de muitos orçamentos em apenas um documento ---#
import os

def limpar_historico():
    confirmacao = input("Tem certeza que deseja todo o historico? (sim/não)"). lower()
    if confirmacao == "sim" or confirmacao == "s":
        if os.path.exists("orcamento.txt"):
            os.remove("orcamento.txt")
            print("Historico deletado com sucesso!")
        else:
            print("O arquivo ainda não existe, então não há o que deletar.")
    else:
        print("Operação cancelada.")      

#--- Construção de Menu da Calculadora ---#
while True:
    print("\n--- Calculadora Freelancer ---")
    print("1. Novo Orçamento")
    print("2. Limpar Histórico")
    print("3. sair")

    opcao = input("Escolha uma opção: ")

    #---VARIAVEIS DO PROJETO + integração do Menu---#
    if opcao == '1':
        projeto = input("Digite o nome do Projeto: ")
        valor_hora = float(input("Qual o valor da sua hora?:"))
        horas_estimadas = int(input("De quantas horas será esse projeto?:"))
        urgente = input("O projeto é urgente?: (sim/não): ")

        valor_total = (valor_hora * horas_estimadas)

        #---Condição de Acrescimo de 20% caso o projeto seja urgente---#
        if urgente == "sim":
            valor_total = valor_total *1.2
            print("Atenção: Adicionado uma taxa de 20% por urgencia!")

        print(f"O valor total do projeto {projeto} é: R$ {valor_total}")
        
        #---Documento Oficial do Orçamento da Calculadora---#
        with open("orcamento.txt", "a") as arquivo:
            arquivo.write("-------ORÇAMENTO FREELANCE-------\n")
            arquivo.write(f"Projeto:{projeto}\n")
            arquivo.write(f"Valor da hora: R$ {valor_hora}\n")
            arquivo.write(f"Horas estimadas:{horas_estimadas}\n")
            arquivo.write(f"Urgente: {urgente}\n")
            arquivo.write("-----------------------------------")
            arquivo.write(f"VALOR TOTAL ESTIMADO: R$ {valor_total}\n")

        print("Orçamento salvo no arquivo 'orcamento.txt'!")

    elif opcao == '2':
        limpar_historico()
    elif opcao == '3':
        break
    else:
        print("Opção invalida! Escolha 1, 1 ou 3.")