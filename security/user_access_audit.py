import csv
import os
import subprocess
from datetime import datetime

arquivo = "user_access_audit.csv"


def criar_arquivo():
    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow([
                "Date",
                "User",
                "Department",
                "System",
                "Access Type"
            ])


def registrar_acesso():
    usuario = input("User Name: ").strip()
    departamento = input("Department: ").strip()
    sistema = input("System: ").strip()
    acesso = input("Access Type (Granted/Removed): ").strip()

    if usuario == "" or sistema == "":
        print("\nFill required fields.\n")
        return

    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(arquivo, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([
            data,
            usuario,
            departamento,
            sistema,
            acesso
        ])

    print("\nAccess recorded successfully.\n")

    # abre o CSV automaticamente
    try:
        subprocess.Popen(arquivo)
    except Exception:
        pass


def visualizar_registros():
    if not os.path.exists(arquivo):
        print("\nNo records found.\n")
        return

    print("\n========== ACCESS LOG ==========\n")

    with open(arquivo, "r", encoding="utf-8") as file:
        print(file.read())


while True:
    criar_arquivo()

    print("=" * 40)
    print("     USER ACCESS AUDIT TOOL")
    print("=" * 40)
    print("1 - Register Access")
    print("2 - View Records")
    print("3 - Exit")
    print("=" * 40)

    opcao = input("Choose an option: ")

    if opcao == "1":
        registrar_acesso()

    elif opcao == "2":
        visualizar_registros()

    elif opcao == "3":
        print("\nClosing system...")
        break

    else:
        print("\nInvalid option.\n")