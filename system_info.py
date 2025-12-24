import platform
import socket
import datetime

def gerar_relatorio():
    # Coletando informações básicas
    nome_maquina = socket.gethostname()
    sistema = platform.system()
    versao = platform.release()
    processador = platform.processor()
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Criando o conteúdo do texto
    relatorio = f"""
    ==========================================
    RELATÓRIO DE INFORMAÇÕES DO SISTEMA
    ==========================================
    Data da Coleta: {data_atual}
    Nome da Máquina: {nome_maquina}
    Sistema Operacional: {sistema} {versao}
    Processador: {processador}
    ==========================================
    """
    
    # Salvando em um arquivo .txt
    with open("info_sistema.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
    
    print("Relatório gerado com sucesso: info_sistema.txt")

if __name__ == "__main__":
    gerar_relatorio()