# this program returns an array of strike price, expiry date, and IV

from APIKEY import APIKEY
import requests

# returns for all calls on a ticker
def getOverallInfo(ticker, limit):

    polygon_api_key = APIKEY.key

    params = {
        'apiKey':polygon_api_key,
        'limit':limit,
        'contract_type':'call'
    }

    url = "https://api.polygon.io/v3/snapshot/options/" + ticker

    # get options chain for ticker
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        output = []

        try:

            for i in range(0, len(data['results'])):
                element = []
                if 'implied_volatility' in data['results'][i]:
                    element.append(data['results'][i]['details']['strike_price'])
                    element.append(data['results'][i]['details']['expiration_date'])
                    element.append(data['results'][i]['implied_volatility'])
                    output.append(element)

        except Exception as e:
            print("issue with " + ticker)
            print(e)

        return output

    else:
        print("failed with code " + str(response.status_code))
        print(response.json())
        return 'faliure'

# returns for calls found at a certain strike price and expiration date
def getSpecificInfo(ticker, limit, strike_price, expiration_date):

    polygon_api_key = APIKEY.key

    params = {
        'apiKey':polygon_api_key,
        'limit':limit,
        'contract_type':'call',
        'strike_price':strike_price,
        'expiration_date':expiration_date
    }

    url = "https://api.polygon.io/v3/snapshot/options/" + ticker

    # get options chain for ticker
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        output = []

        try:

            for i in range(0, len(data['results'])):
                element = []
                if 'implied_volatility' in data['results'][i]:
                    element.append(data['results'][i]['details']['strike_price'])
                    element.append(data['results'][i]['details']['expiration_date'])
                    element.append(data['results'][i]['implied_volatility'])
                    output.append(element)

        except Exception as e:
            print("issue with " + ticker)
            print(e)

        return output

    else:
        print("failed with code " + str(response.status_code))
        print(response.json())
        return 'faliure'