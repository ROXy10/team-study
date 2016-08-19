import requests


def api_request(query='kiev'):
    # String. Skyscanner country code(ISO code).
    market = 'UA'
    # String. ISO currency code(example ‘GBP’, ‘USD’).See the the Currencies Service for supported currencies.
    currency = 'UAH'
    # String. ISO locale code(example ‘en - GB’).
    locale = 'uk-UA'
    # String. At least two characters long
    api_key = 'oo309997673678373155996964049648'

    http_request = "http://partners.api.skyscanner.net/apiservices/hotels/autosuggest/v2/%s/%s/%s/%s?apikey=%s" % (
    market, currency, locale, query, api_key)

    try:
        response = requests.get(http_request, timeout=10)
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
        return False
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')
        return False

    response_json = response.json()
    for result in response_json['results']:
        if result['geo_type'] == 'Airport':
            print(result['display_name'])


api_request('mos')
