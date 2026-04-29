import os
from datetime import datetime

arquivo = "daily_it_tasks.txt"


def salvar_tarefa(usuario, setor, tarefa, prioridade):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(arquivo, "a", encoding="utf-8") as file:
        file.write(f"{data} | {usuario} | {setor} | {tarefa} | {prioridade}\n")


def mostrar_tarefas():
    if not os.path.exists(arquivo):
        print("\nNenhuma tarefa registrada ainda.\n")
        return

    print("\n========== TASK HISTORY ==========\n")

    with open(arquivo, "r", encoding="utf-8") as file:
        print(file.read())


while True:
    print("=" * 40)
    print("      DAILY IT TASK LOGGER")
    print("=" * 40)
    print("1 - Register Task")
    print("2 - View History")
    print("3 - Exit")
    print("=" * 40)

    opcao = input("Choose an option: ")

    if opcao == "1":
        usuario = input("Technician Name: ").strip()
        setor = input("Department: ").strip()
        tarefa = input("Task Performed: ").strip()
        prioridade = input("Priority (Low/Medium/High): ").strip()

        if usuario == "" or tarefa == "":
            print("\nFill required fields.\n")
            continue

        salvar_tarefa(usuario, setor, tarefa, prioridade)

        print("\nTask registered successfully.\n")

    elif opcao == "2":
        mostrar_tarefas()

    elif opcao == "3":
        print("\nClosing system...")
        break

    else:
        print("\nInvalid option.\n")