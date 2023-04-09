# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mhvillage.com/mobile-homes"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the mobile home listings on the page
listings = soup.find_all("div", {"class": "home-info"})

# Print the details of each mobile home listing
for listing in listings:
    print("Title:", listing.find("h2").text.strip())
    print("Price:", listing.find("div", {"class": "home-price"}).text.strip())
    print("Location:", listing.find("div", {"class": "home-location"}).text.strip())
    print("Bedrooms:", listing.find("div", {"class": "home-bedrooms"}).text.strip())
    print("Bathrooms:", listing.find("div", {"class": "home-bathrooms"}).text.strip())
    print("Square Feet:", listing.find("div", {"class": "home-square-feet"}).text.strip())
    print("---------------------------------------")
