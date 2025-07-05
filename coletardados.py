def coletardados():
    from datetime import datetime

    nome = str(input("Digite seu nome:").strip().lower())
    
    while True:
        try:
            idade = int(input("Digite sua idade:"))
            break
        except ValueError:
            print("Digite apenas sua idade com números!")

    while True:
        aniversario = input("Digite sua data de nascimento (dd/mm/aaaa):")
        try:
            dataniver = datetime.strptime(aniversario, "%d/%m/%Y").date()
            dataniver = dataniver.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato inválido. O correto é dd/mm/aaaa.")

    dia_entrada = datetime.now().strftime("%d/%m/%Y")

    while True:
        try:
            dependentes = str(input("Você está acompanhado(a) de algum não pagante? Responda com Sim ou Não.").strip().lower())
            resposta = dependentes.split()[0]
            if resposta in ["s", "sim"]:
                acompanhantes = []
                numero = int(input("Quantos dependentes estão com você?"))
                for a in range(numero):
                    nomedep = str(input("Digite o nome do(a) dependente:"))
                    acompanhantes.append(nomedep)
            if resposta in ["n", "nao", "não"]:
                acompanhantes = []
            break
        except:
            print("Resposta inválida. Entre com Sim ou Não.")

    return nome, idade, dataniver, dia_entrada, acompanhantes

coletardados()