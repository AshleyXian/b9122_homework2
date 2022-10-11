from bs4 import BeautifulSoup
import urllib.request

from HW2.CheckWordInPage import find_word

seed_url = "https://www.sec.gov/news/pressreleases"
new_seed_url = "https://www.sec.gov/news/pressrelease"

urls = [seed_url]  # queue of urls to crawl
seen = [seed_url]  # stack of urls seen so far
opened = []  # we keep track of seen urls so that we don't revisit them
res = []  # the result list of urls

maxNumUrl = 20  # set the maximum number of urls to visit

while len(urls) > 0 and len(res) < maxNumUrl:
    try:
        curr_url = urls.pop(0)
        req = urllib.request.Request(curr_url,
                                     headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:
        print("Unable to access= " + curr_url)
        print(ex)
        continue

    soup = BeautifulSoup(webpage, "lxml")  # creates object soup
    if find_word(soup, "charges"):
        res.append(curr_url)
        print("Found one: " + curr_url)

    for tag in soup.find_all('a', attrs={"hreflang": "en"},
                             href=True):  # find tags with links
        childUrl = tag['href']  # extract just the link
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(new_seed_url, childUrl)

        if new_seed_url in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)

print("num. of res URLs = %d, and scanned = %d" % (len(res), len(opened)))
print(len(seen))
print("List of seen URLs:")
for res_url in res:
    print(res_url)
