from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
dict_tempo_operacao = {}
numero_saques = 0
LIMITE_SAQUES = 3


def adiciona_operacao_com_tempo(dict, operacao):
    """Adiciona uma operacao ao dict, usando como chave o tempo atual"""
    tempo_agora = datetime.now()
    if dict.__contains__(tempo_agora):
        dict[tempo_agora].append(operacao)
    else:
        dict[tempo_agora] = [operacao]

def exibir_extrato(dict):
    for tempo, operacao in dict.items():
        print(f"{tempo:%d-%m-%Y %H:%M:%S} - {operacao}")

while True:

    opcao = input(menu).lower()

    match opcao:
        case "d" | "depositar":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                adiciona_operacao_com_tempo(dict_tempo_operacao, f"Depósito: R$ {valor:.2f}")

            else:
                print("Operação falhou! O valor informado é inválido.")
        case "s" | "sacar":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                adiciona_operacao_com_tempo(dict_tempo_operacao, f"Saque: R$ {valor:.2f}")
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        case "e" | "extrato":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações.") if not dict_tempo_operacao else exibir_extrato(dict_tempo_operacao)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
        case "q" | "sair":
            break
        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

        
