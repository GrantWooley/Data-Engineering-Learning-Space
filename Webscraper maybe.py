from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#Get full html from the page

URL = 'http://olympus.realpython.org/profiles'

HTML = urlopen(URL)

Soup = BeautifulSoup(HTML,"html.parser")

tags = list(Soup.find_all("a"))
#print(tag1.name)
#print(tag1.attrs)
#print(tag1['href'])

URLs = [ URL + tag['href'].split('/profiles')[1] for tag in tags]

for x in URLs:
    print(x)

"""
Using Beautiful Soup, print out a list of all the links on the page by looking for HTML tags with the name a and retrieving the value taken on by the href attribute of each tag.
should look like the following:
http://olympus.realpython.org/profiles/aphrodite
http://olympus.realpython.org/profiles/poseidon
http://olympus.realpython.org/profiles/dionysus

"""