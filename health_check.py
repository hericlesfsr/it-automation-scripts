import os  ## Permite interagir com o Sistema Operacional.
import shutil  ## Usado para utilitários de arquivos e pastas (neste caso, para medir o espaço em disco).
import socket  ## É a ferramenta para conexões de rede e protocolos de comunicação.

def verificar_disco():
    # Verifica o disco C:
    total, usado, livre = shutil.disk_usage("C:") ## Esta linha "pergunta" ao computador sobre o drive C:. Ela retorna três valores de uma vez, que são guardados em três variáveis diferentes:
    gb_livre = livre // (2**30) # Converte bytes para GB usando divisão inteira - O Windows mede o espaço em bytes (um número gigante). Para transformar em GigaBytes (GB), dividimos por $2^{30}$. O uso do // garante que o resultado seja um número inteiro, facilitando a leitura.
    
    if gb_livre < 10:
        print(f"ALERTA: Pouco espaço em disco! Apenas {gb_livre}GB livres.")
    else:
        print(f"Espaço em disco OK: {gb_livre}GB livres.")

def verificar_rede():
    # Tenta conectar ao DNS do Google para testar a internet
    try: ## O Python tenta executar a conexão.
        socket.create_connection(("8.8.8.8", 53), timeout=3) ## O código tenta "bater na porta" do DNS do Google (8.8.8.8). Se ele responder em até 3 segundos, a conexão está ativa.
        print("Conexão de rede: OK (Internet funcional).")
    except OSError: ## Se a internet estiver caída, o Python daria um erro e fecharia o programa. O except captura esse erro ("exceção") e, em vez de travar tudo, ele apenas imprime o aviso de "ALERTA".
        print("ALERTA: Sem conexão com a internet!")

print("--- INICIANDO VERIFICAÇÃO DE SAÚDE DO SISTEMA ---")
verificar_disco()
verificar_rede()
print("--- VERIFICAÇÃO CONCLUÍDA ---")