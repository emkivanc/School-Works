import urllib.request
def connect(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
links =  ['​https://api.github.com​', '​http://bilgisayar.mu.edu.tr/​', 'https://www.python.org/​', 'http://akrepnalan.com/ceng2034​', '​https://github.com/caesarsalad/wow​']
for host in links:
  print( 'Connected succesfully.' if connect(host) else 'Link does not work.' )

import requests
from requests.exceptions import HTTPError

for url in ['​https://api.github.com​', '​http://bilgisayar.mu.edu.tr/​', 'https://www.python.org/​', 'http://akrepnalan.com/ceng2034​', '​https://github.com/caesarsalad/wow​']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')