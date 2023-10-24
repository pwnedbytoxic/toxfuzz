import requests
import sys

def loop():
    for element in sys.stdin:
        res = requests.get(url=f"https://example.com/api/{element}")
        if res.status_code == 404:
            loop()

        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(element)
loop()