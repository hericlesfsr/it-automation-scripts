from datetime import datetime

total = 0.0

while True:

    print("\n" + "-" * 15, "CONTROLE DE GASTOS", "-" * 15)
    print("\n1 - Adicionar gasto")
    print("2 - Ver histórico de gastos")
    print("3 - Ver total gasto")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        try:
            nome = input("\nNome do gasto: ")
            valor = float(input("Valor do gasto: R$"))

            if valor <= 0:
                print("Digite um valor válido.")
                continue

            data = datetime.now().strftime("%d/%m/%Y %H:%M")

            print("\nGasto registrado com sucesso!")

            total += valor

            with open("gastos.txt", "a") as arquivo:
                arquivo.write(f"{data} | {nome} | R${valor:.2f}\n")

        except ValueError:
            print("Digite um valor numérico.")

    elif opcao == "2":

        try:
            with open("gastos.txt", "r") as arquivo:

                print("\n--- HISTÓRICO DE GASTOS ---\n")

                for linha in arquivo:
                    print(linha.strip())

        except FileNotFoundError:
            print("\nNenhum gasto registrado ainda.")

    elif opcao == "3":
        print(f"\nTotal gasto nesta sessão: R${total:.2f}")

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")