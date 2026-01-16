import requests
import time
from datetime import datetime

def check_website():
    url = "https://www.google.com"
    print(f"Checking connectivity for: {url}")

    # Loop para testar 3 vezes
    for i in range(3):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            latency = round((time.time() - start_time) * 1000)
            
            current_time = datetime.now().strftime("%H:%M:%S")
            status = "ONLINE" if response.status_code == 200 else "OFFLINE"

            result = f"[{current_time}] Attempt {i+1}: {status} | Latency: {latency}ms"
            print(result)

            with open("web_monitor_log.txt", "a", encoding="utf-8") as file:
                file.write(result + "\n")

            # Espera 5 segundos antes de testar novamente
            if i < 2: 
                time.sleep(5)

        except Exception as e:
            print(f"Error: {e}")
            break

    print("\nCheck finished. Data saved to web_monitor_log.txt")

if __name__ == "__main__":
    check_website()