import bs4
import urllib.request

URL = "http://py4e-data.dr-chuck.net/comments_1734129.html"

with urllib.request.urlopen(URL) as f:
    page = f.read()

soup = bs4.BeautifulSoup(page, features="html.parser")
spans = soup("span")

sum_of_integers = sum([int(span.text) for span in spans])

print(sum_of_integers)
