# Python 3.6.4
# Downloads the newest XKCD comic as an example of 
# web-scraping and downloading a file.
import urllib.request
import requests
from bs4 import BeautifulSoup


def newest_xkcd():
    url = "https://www.xkcd.com/"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    # Examines the website.
    image = soup.find("div", id="comic").img['src']  # Finds the file URL.
    image = f"http://{image[2:]}"  # Fixes the prefix to the URL.
    f = open('XKCD_img.jpg', 'wb')
    f.write(requests.get(image).content)  # Saves the file locally.
    f.close()


newest_xkcd()
