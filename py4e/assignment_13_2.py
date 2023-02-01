import json
import urllib.request

url = input("Enter URL: ")


def open_page(url: str) -> str:
    with urllib.request.urlopen(url) as f:
        print(f"Retrieving {url}")
        page = f.read()
    return page


def parse_page(page):
    return json.loads(page)


def comments(page_json) -> list[dict[str, int]]:
    return page_json["comments"]


def sum_comments(comments: list[dict[str, int]]) -> int:
    return sum([item["count"] for item in comments])


page = open_page(url)
page_json = parse_page(page)
page_comments = comments(page_json)
total = sum_comments(page_comments)

print(f"Sum {total}")
