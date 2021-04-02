from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
 


def scrape():
    browser = init_browser()
    listings = {}

    # import os
    # from bs4 import BeautifulSoup as bs
    # from bs4 import BeautifulSoup
    # import requests

    # from splinter import Browser
    # from bs4 import BeautifulSoup
    # from webdriver_manager.chrome import ChromeDriverManager
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)


    # %%
    # URL of page to be scraped
    # url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

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
    news_title = soup.find("li", class_ ="slide")
    news_title_text = news_title.find("div",class_="content_title").find("a").text
    news_title_text


    # %%

    print(url + 'system/news_items/list_view_images/8896_thumb-320.jpg')


    # %%
    #2.Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Paragraph Text. Assign the text to variables that you can reference later.

    news_p = soup.find("li", class_ ="slide").text
    news_p


    # %%
    imagetag = soup.find("li", class_ ="slide")
    img_tag = imagetag.find("img")
    img_tag


    # %%
    titletag = soup.find("li", class_ ="slide")
    titletag_text = titletag.find("div",class_="content_title").find("a").text
    titletag_text


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
    feature_image = url[:-10] + feature
    feature_image

    ### Mars Facts
    # * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.*

    # import requests
    # import os
    # import bs4
    # import string
    # import pandas as pd
    # import numpy as np
    # import requests
    # from bs4 import BeautifulSoup
    # from time import sleep


    # # %%
    url = 'https://space-facts.com/mars'

    response = requests.get(url)

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

    from splinter import Browser
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager
    

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)

    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')

    print(soup2.prettify())

    # %%
    from bs4 import BeautifulSoup
    import requests
    import pymongo

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.mars_db
    collection = db.post

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Retrieve page with the requests module
    response2 = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup4 = BeautifulSoup(response2.text, 'lxml')

    # %%
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
    ]

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "feature_image": feature_image,
        "html_table": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
        }


    # browser.quit()
    return mars_data

    browser.visit(url).quit()


