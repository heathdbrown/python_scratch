import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")


def open_page(url: str) -> str:
    with urllib.request.urlopen(url) as f:
        print(f"Retrieving {url}")
        page = f.read()
    return page


def parse_page(page):
    return ET.fromstring(page)


def sum_integers(xml) -> int:
    return sum([int(child.text) for child in xml.findall(".//count")])


print(sum_integers(parse_page(open_page(url))))
