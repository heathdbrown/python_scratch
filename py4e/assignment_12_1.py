import httpx

URL = "http://data.pr4e.org/intro-short.txt"

site = httpx.get(URL)

last_modified = site.headers["last-modified"]
etag = site.headers["etag"]
content_length = site.headers["content-length"]
cache_control = site.headers["cache-control"]
content_type = site.headers["content-type"]

print(last_modified)
print(etag)
print(content_length)
print(cache_control)
print(content_type)
