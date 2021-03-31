# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
import os
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import requests

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

 


# %%
# !pip install urlib2


# %%
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# URL of page to be scraped
# url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
url = 'https://mars.nasa.gov/news/'

browser.visit(url)


# %%
# Retrieve page with the requests module
response = requests.get('https://mars.nasa.gov/system/news_items/list_view_images/8896_thumb-320.jpg')

response

# %% [markdown]
# # Create BeautifulSoup object; parse with 'html.parser'
# soup = BeautifulSoup(browser.html, 'html.parser')
# 

# %%
soup = BeautifulSoup(browser.html, 'html.parser')


# %%
# Examine the results, then determine element that contains sought info
print(soup.prettify())


# %%
#1. Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title
news_title = soup.find_all("li",class_ = "slide")
for everyli in news_title:
    # print(everyli)
    print(everyli.find("h3").text)
    img_source = everyli.find("div", class_="list_image").img["src"]
    print(url[:-5] + img_source)
    print("-"*20)
  
    
    


# %%

print(url + 'system/news_items/list_view_images/8896_thumb-320.jpg')


# %%
titletag = soup.find("li", class_ ="slide")
titletag


# %%

# atag = titletag.find('a')

# "https://mars.nasa.gov/news/" + atag["href"] 


# %%
#2.Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Paragraph Text. Assign the text to variables that you can reference later.

news_p = soup.find_all("div",class_ = "article_teaser_body")
# print(news_p)

for p in news_p:
    print(p.text)
    print("-"*20)


# %%
imagetag = soup.find("li", class_ ="slide")
img_tag = imagetag.find("img")
img_tag


# %%
titletag = soup.find("li", class_ ="slide")
titletag.find("div",class_="content_title").find("a").text


# %%

local_path = titletag.find_all("img")
for img in local_path:
    print(img)


# '/assets/overlay-arrow.png'


# %%
# JPL Mars Space Images - Featured Image

#* Mars Facts


# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


# Use Pandas to convert the data to a HTML table string.


# %%
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# %%
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

browser.visit(url)


# %%
response1 = requests.get(url)
response


# %%
soup1 = BeautifulSoup(browser.html, 'html.parser')


# %%
print(soup1.prettify())


# %%
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

browser.visit(url)


html = browser.html
soup1 = BeautifulSoup(html, 'html.parser')


# %%
featured_images = soup1.find_all('img', class_='headerimage fade-in')
feature = featured_images[0].attrs['src']
print(url[:-10] + feature)


# %%
### Mars Facts
# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.*


# %%
import requests
import os
import bs4
import string
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep


# %%
url = 'https://space-facts.com/mars'

response = requests.get(url)


# %%
response


# %%
#Use Pandas to convert the data to a HTML table string.
tables = pd.read_html(url)
tables


# %%
type(tables)


# %%
df = tables[0]
df.head()


# %%
tables = pd.read_html(url)
df = tables[0]
html_table = df.to_html()
html_table


# %%
### Mars Hemispheres

# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.


# %%
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import attr


# %%
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)


html = browser.html
soup2 = BeautifulSoup(html, 'html.parser')


# %%
print(soup2.prettify())


# %%
astr_title = soup2.find_all("div",class_ = "description")
#for title in astr_title:

astr_title[0].find("h3")
y = astr_title[0].find('a').attrs['href']
z='https://astrogeology.usgs.gov' + y
browser.visit(z)
html = browser.html
soup3 = BeautifulSoup(html, 'html.parser')
e = soup3.find('img', class_ ="wide-image")
u = e.attrs['src']
t = 'https://astrogeology.usgs.gov' + u
t


# %%



# %%

for title in astr_title:
    img_link = title.find("h3").text
    print(img_link)


# %%
image_title = soup2.find_all('img', class_ ='thumb')
for image in image_title:
    # print(everyli)
    # img_source = image.find('h3').text
    # print(image.find('h3').text)
    print('https://astrogeology.usgs.gov' + image['src'])
    # img_link = image.find('a', class_='thumb')
    print("-"*20)

    # <img class="thumb description-thumb" src="/cache/images/f789a481f60deaf01996343999491211_valles_marineris_unenhanced.tif_thumb.png" alt="Valles Marineris Hemisphere Unenhanced thumbnail">


# %%
for item in image_title:
    # if item['src'][:6]=='/cache':
    print(item['src'])


# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup
  
htmldata = urlopen('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/')
soup2 = BeautifulSoup(htmldata, 'html.parser')
image_title = soup2.find_all('h3', class_='description')
print(image_title)
images = soup2.find_all('img')

  
for item in images:
    print(image_title)
    print(item['src'])
    print("-"*20)


# %%
from bs4 import BeautifulSoup
import requests
import pymongo


# %%
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# %%
db = client.mars_db
db.mars.drop()
collection = db.post


# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

# Retrieve page with the requests module
response2 = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup4 = BeautifulSoup(response2.text, 'lxml')


# %%
# results = soup4.find_all('div', class_='caption')


# %%
results = soup4.find_all('div', class_='container')

# Loop through returned results
for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        title = result.find('h2', class_='title')
        # Identify and return price of listing
        full_image = result.find('img', class_='wide-image')
        # Identify and return link to listing
        link = result.a['href']

        # Run only if title, price, and link are available
        if (title and full_image and link):
            # Print results
            print('-------------')
            print(title)
            print(full_image)
            print(link)

            # Dictionary to be inserted as a MongoDB document
            post = {
                'title': title,
                'full_image': full_image,
                'url': link
            }

            collection.insert_one(post)

    except Exception as e:
        print(e)


# %%
hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
]


# %%
collection.insert_many(hemisphere_image_urls)

browser.quit()
# %%



