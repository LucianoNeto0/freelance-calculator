#---VARIAVEIS DO PROJETO---#
projeto = input("Digite o nome do Projeto:")
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
with open("orcamento.txt", "w") as arquivo:
    arquivo.write("-------ORÇAMENTO FREELANCE-------\n")
    arquivo.write(f"Projeto:{projeto}\n")
    arquivo.write(f"Valor da hora: R$ {valor_hora}\n")
    arquivo.write(f"Horas estimadas:{horas_estimadas}\n")
    arquivo.write(f"Urgente: {urgente}\n")
    arquivo.write("-----------------------------------")
    arquivo.write(f"VALOR TOTAL ESTIMADO: R$ {valor_total}\n")
