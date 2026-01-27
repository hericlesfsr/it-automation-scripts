import socket
import sys
from datetime import datetime

def scan_ports(target_host):
    # Lista de portas comuns para testar (HTTP, HTTPS, FTP, SSH, RDP)
    common_ports = [21, 22, 23, 80, 443, 3389, 8080]
    
    print("-" * 50)
    print(f"Scanning Target: {target_host}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        for port in common_ports:
            # Cria um socket para testar a conexão
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # Espera apenas 1 segundo por porta
            
            # Tenta conectar na porta
            result = s.connect_ex((target_host, port))
            
            if result == 0:
                status = f"Port {port}: OPEN"
            else:
                status = f"Port {port}: CLOSED"
            
            print(f"[+] {status}")
            
            # Salva no log para auditoria
            with open("security_scan_log.txt", "a", encoding="utf-8") as log:
                log.write(f"[{datetime.now()}] Host: {target_host} | {status}\n")
            
            s.close()

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nServer not responding.")
        sys.exit()

if __name__ == "__main__":
    # Você pode testar no 'localhost' (seu próprio PC) ou no seu roteador
    target = "localhost" 
    scan_ports(target)
    print("\nScan complete. Results saved to security_scan_log.txt")