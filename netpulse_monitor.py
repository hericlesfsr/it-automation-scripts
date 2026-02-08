import os
import time
import platform
import subprocess
from datetime import datetime

def ping_host(host):
    # Determina o parâmetro do comando ping baseada no Sistema Operacional
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    
    try:
        # Executa o ping e captura a saída
        start_time = time.time()
        output = subprocess.check_output(command).decode('latin-1')
        end_time = time.time()
        
        # Calcula latência em milissegundos
        latency = round((end_time - start_time) * 1000, 2)
        return latency
    except Exception:
        return None

def start_monitor(target="8.8.8.8", threshold=100):
    print(f"--- Iniciando Monitoramento de Rede: {target} ---")
    print(f"Alerta configurado para latência acima de: {threshold}ms\n")

    try:
        while True:
            latency = ping_host(target)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            if latency is None:
                status = "🔴 QUEDA DE CONEXÃO"
            elif latency > threshold:
                status = f"⚠️ LATÊNCIA ALTA: {latency}ms"
            else:
                status = f"✅ ESTÁVEL: {latency}ms"

            log_entry = f"[{timestamp}] {status}"
            print(log_entry)

            # Salva em log para auditoria posterior (estilo port scanner)
            with open("network_health.log", "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")

            time.sleep(2) # Intervalo entre verificações
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")

if __name__ == "__main__":
    # 8.8.8.8 é o DNS do Google, ótimo para testar estabilidade
    start_monitor("8.8.8.8", threshold=80)