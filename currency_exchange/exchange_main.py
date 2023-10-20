from urllib.request import urlopen
from json import loads
from datetime import datetime

ExchangeRate_API = "https://v6.exchangerate-api.com/v6/af1801f26a08eab0fe06b8ed/latest/USD"

ExchangeRate = urlopen(ExchangeRate_API)
now = datetime.now()
current_time = now.strftime("%A %d %b %Y, %I:%M%p")


bytes = ExchangeRate.read()

json = bytes.decode("utf-8")

rates = loads(json)

print(f"\n\nExchange rates as of {current_time}.")
print(f"Importing exchange rates: {rates['result']}")
print("\nAvailable currencies:")

currencies = [x for x in rates['conversion_rates']]

currencies_neat = ["\n"]
for i in currencies:
    currencies_neat.append(i)
    currencies_neat.append("\t")
    if len(currencies_neat) % 37 == 0:
        currencies_neat.append("\n")
print("".join(currencies_neat))

from_currency = ""
to_currency = ""
while True:
    from_currency = input("\nWhich currency do you want to convert from? >")
    if from_currency.upper() in currencies:
        break
    print("That is not an available currency.")

while True:
    to_currency = input("\nWhich currency do you want to convert to? >")
    if to_currency.upper() in currencies:
        break
    print("That is not an available currency.")

amount = 0
while True:
    amount = input("\nAmount to be converted: >")
    if amount.replace(".","").isnumeric():
        amount = float(amount)
        break
    print("That is not a valid number.")

print("\n",from_currency, to_currency, amount)

# conversion = to / from
conversion = rates['conversion_rates'][to_currency] / rates['conversion_rates'][from_currency] * amount
print(f"\n{amount} in {from_currency} is equal to {conversion} in {to_currency}")
