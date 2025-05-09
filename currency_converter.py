import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Error: Failed to fetch exchange rate.")
        return None

    data = response.json()
    return data.get("result")

def main():
    print("💱 Currency Converter")
    try:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            print("❌ Conversion failed.")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

if __name__ == "__main__":
    main()
