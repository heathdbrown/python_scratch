import json
import urllib.parse
import urllib.request

API_URL = "http://py4e-data.dr-chuck.net/json?"

location = input("Enter location: ")

params = dict()
params["address"] = location
params["key"] = 42

url = API_URL + urllib.parse.urlencode(params)


def open_page(url: str) -> str:
    with urllib.request.urlopen(url) as f:
        print(f"Retrieving {url}")
        page = f.read()
    return page


def parse_page(page):
    return json.loads(page)


def place_id(page_json):
    return page_json["results"][0]["place_id"]


print(place_id(parse_page(open_page(url))))
