import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://ibjjf.com/events/results'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')


print(soup)