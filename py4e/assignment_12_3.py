import bs4
import urllib.request

url = input("Enter URL: ")
count = int(input("Enter count: ")) + 1
position = int(input("Enter position: "))
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"


def open_page(url: str) -> str:
    with urllib.request.urlopen(url) as f:
        print(f"Retrieving {url}")
        page = f.read()
    return page


def links_on_page(page) -> list[bs4.Tag]:
    soup = bs4.BeautifulSoup(page, features="html.parser")
    links = soup("a")
    return links


def link_at_position(links: list[bs4.Tag], position: int):
    return links[position - 1]["href"]


for _ in range(count):

    page = open_page(url)

    links = links_on_page(page)

    loop = 0
    for link in links:
        loop = loop + 1

        if loop > position:
            break
        url = link_at_position(links, position)
