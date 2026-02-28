from datetime import datetime

data_atual = datetime.now().strftime("%d-%m-%Y")
nome_arquivo = f"folha_pagamento_{data_atual}.txt"

print(f"\n{' SEJA BEM-VINDO AO CÁLCULO SALARIAL ':=^70}")

while True:

    funcionario = input("\nDigite o nome do(a) funcionário(a): ")
    valor_hora = float(input("Qual o salário por hora? R$ "))
    horas_mes = float(input("Quantas horas foram trabalhadas no mês? "))

    salario_bruto = valor_hora * horas_mes

    # --- INSS ---
    if salario_bruto <= 1621.00:
        aliquota_inss = 0.075
    elif salario_bruto <= 2902.84:
        aliquota_inss = 0.09
    elif salario_bruto <= 4354.27:
        aliquota_inss = 0.12
    else:
        aliquota_inss = 0.14

    inss = salario_bruto * aliquota_inss

    teto_inss = 8475.55 * 0.14
    if inss > teto_inss:
        inss = teto_inss

    # --- IRRF ---
    base_irrf = salario_bruto - inss
    irrf = 0
    aliquota_ir_texto = "Isento"

    if base_irrf <= 2824.00:
        irrf = 0
        aliquota_ir_texto = "0%"
    elif base_irrf <= 3751.05:
        irrf = (base_irrf * 0.15) - 394.16
        aliquota_ir_texto = "15%"
    elif base_irrf <= 4664.68:
        irrf = (base_irrf * 0.225) - 675.49
        aliquota_ir_texto = "22,5%"
    else:
        irrf = (base_irrf * 0.275) - 908.73
        aliquota_ir_texto = "27,5%"

    if irrf < 0:
        irrf = 0

    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - inss - irrf - sindicato

    # Exibição
    print(f"\n{' RESULTADO DO CONTRACHEQUE ':=^40}")
    print(f"Funcionário      : {funcionario}")
    print(f"Salário Bruto    : R$ {salario_bruto:>10.2f}")
    print(f"(-) INSS         : R$ {inss:>10.2f}")
    print(f"(-) IRRF         : R$ {irrf:>10.2f}")
    print(f"(-) Sindicato    : R$ {sindicato:>10.2f}")
    print(f"{'-'*40}")
    print(f"Salário Líquido  : R$ {salario_liquido:>10.2f}")

    # Gravar no TXT sem apagar o anterior
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write("\n" + "="*50 + "\n")
        arquivo.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        arquivo.write(f"Funcionário: {funcionario}\n")
        arquivo.write(f"Salário Bruto: R$ {salario_bruto:.2f}\n")
        arquivo.write(f"INSS: R$ {inss:.2f}\n")
        arquivo.write(f"IRRF: R$ {irrf:.2f}\n")
        arquivo.write(f"Sindicato: R$ {sindicato:.2f}\n")
        arquivo.write(f"Salário Líquido: R$ {salario_liquido:.2f}\n")

    # Pergunta para continuar
    continuar = input("\nDeseja calcular outro funcionário? (s/n): ").strip().lower()

    if continuar != "s":
        print("\nEncerrando sistema... Arquivo salvo com sucesso ✅")
        break