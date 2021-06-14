from bs4 import BeautifulSoup
import requests

url = 'https://www.rbauction.com/?keywords=ex200'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
# print(soup.prettify()) # Prints lots of cruft

links = soup.find_all("a")
for link in links:
    link_text = link.get("href")
    if link_text is None:   # Handle an artifact of lxml
        continue
    #if "http" in link_text:
    print("<a href='%s'>%s</a>" % (link_text, link.text))

# searches = soup.find_all("div", {"class": "row"})
# searches = soup.find_all("div")
# searches = soup.find_all("section", {"class": "search-results-item"})
#searches = soup.find_all("section")

#for item in searches:
#   print(item.text)
