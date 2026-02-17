import psutil
import time
import os

def monitor_system():
    try:
        while True:
            # Coleta de dados
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Limpa o terminal para o efeito de "dashboard"
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("=== MONITOR DE RECURSOS EM TEMPO REAL ===")
            
            # Barra de progresso visual para CPU
            cpu_bar = '█' * int(cpu_usage / 5) + '-' * (20 - int(cpu_usage / 5))
            print(f"CPU:    [{cpu_bar}] {cpu_usage}%")
            
            # Barra de progresso visual para Memória
            mem_bar = '█' * int(memory.percent / 5) + '-' * (20 - int(memory.percent / 5))
            print(f"RAM:    [{mem_bar}] {memory.percent}%")
            
            # Alerta crítico
            if cpu_usage > 80 or memory.percent > 90:
                print("\n⚠️  ALERTA: USO DE RECURSOS ELEVADO!")
            
            print("\n(Pressione Ctrl+C para encerrar)")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")

if __name__ == "__main__":
        monitor_system()