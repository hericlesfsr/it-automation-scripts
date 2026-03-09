import socket
import platform
import os


def obter_nome_maquina():
    return socket.gethostname()


def obter_ip():
    return socket.gethostbyname(socket.gethostname())


def obter_sistema():
    return platform.system()


def obter_versao():
    return platform.version()


def obter_usuario():
    return os.getlogin()



def main():

    print(33 * "=")
    print("INVENTÁRIO BÁSICO DA MÁQUINA")
    print(33 * "=")
    print()

    nome = obter_nome_maquina()
    ip = obter_ip()
    sistema = obter_sistema()
    versao = obter_versao()
    usuario = obter_usuario()

    print(f"Nome da máquina: {nome}")
    print(f"IP da máquina: {ip}")
    print(f"Sistema operacional: {sistema}")
    print(f"Versão do sistema: {versao}")
    print(f"Usuário logado: {usuario}")

    # Salvando as informações em um arquivo TXT
    with open("inventario_maquina.txt", "w", encoding="utf-8") as arquivo:

        arquivo.write("INVENTÁRIO DA MÁQUINA\n")
        arquivo.write("======================\n\n")

        arquivo.write(f"Nome da máquina: {nome}\n")
        arquivo.write(f"IP da máquina: {ip}\n")
        arquivo.write(f"Sistema operacional: {sistema}\n")
        arquivo.write(f"Versão do sistema: {versao}\n")
        arquivo.write(f"Usuário logado: {usuario}\n")

    print("\nInventário salvo em: inventario_maquina.txt")


if __name__ == "__main__":
    main()