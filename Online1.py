import sys
import requests
from os import rename
import math



r = requests.get("https://coreyms.com")
print(r.status_code)

