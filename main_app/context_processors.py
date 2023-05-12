import requests

def exchange_rates(request):
    url = 'https://api.exchangerate.host/latest'
    currencies_to_display = ['USD', 'GBP', 'JPY']
    response = requests.get(url)
    data = response.json()
    rates = {currency: rate for currency, rate in data['rates'].items() if currency in currencies_to_display}
    return {'exchange_rates': rates}
