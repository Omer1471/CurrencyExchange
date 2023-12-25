import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

def convert_currency(amount, from_currency, to_currency):
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest"
    querystring = {"from": from_currency, "to": to_currency}
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Error: Unable to fetch exchange rates"

# Example usage
amount = 200  # or get this from user input
from_currency = "GBP"  # or get this from user input
to_currency = "USD"  # or get this from user input
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"Converted Amount: {converted_amount}")

