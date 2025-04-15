from http.client import responses

import requests

respons = requests.get('https://qa.freenance.store/api/v1/currency/')
print(respons.status_code)
