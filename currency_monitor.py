import requests
import datetime

def get_exchange_rates():
    print("Fetching current exchange rates...")
    
    # AwesomeAPI URL (USD, EUR, and BTC to BRL)
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    
    try:
        # Making the request
        response = requests.get(url)
        data = response.json()

        # Extracting values
        usd = data['USDBRL']['bid']
        eur = data['EURBRL']['bid']
        btc = data['BTCBRL']['bid']
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        report = (
            f"--- MARKET UPDATE ({current_time}) ---\n"
            f"USD: R$ {float(usd):.2f}\n"
            f"EUR: R$ {float(eur):.2f}\n"
            f"BTC: R$ {float(btc):.2f}\n"
            f"{'-' * 40}\n"
        )

        # Print to terminal
        print(report)

        # Save to history file (append mode)
        with open("currency_history.txt", "a", encoding="utf-8") as file:
            file.write(report)
            
        print("Data successfully saved to 'currency_history.txt'.")

    except Exception as e:
        print(f"Error fetching data from API: {e}")

if __name__ == "__main__":
    get_exchange_rates()