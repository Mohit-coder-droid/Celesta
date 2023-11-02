import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.netmeds.com/catalogsearch/result/paracetamol/all"

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

