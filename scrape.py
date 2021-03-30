from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import scrape_mars
import html
import index.html


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Explore mars.herokuapp.com
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get news_title
    news_title = news_title.find("div",class_="content_title").find("a").text

    # Get the title tag
    titletag = soup.find("li", class_ ="slide").text

    # Get the news paragrapgh
    news_p = soup.find("li", class_ ="slide").text

    # Get the max avg temp
    img_tag = imagetag.find("img")

    # Find feature image
    feature_image = url[:-10] + feature

    #Get mars data table
    html_table = df.to_html()

    # Hemisphere images urls

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astrogeology.usgs.gov/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
    ]
    # costa_data = {
    #     "sloth_img": sloth_img,
    #     "min_temp": min_temp,
    #     "max_temp": max_temp
    # }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

    "title": news_title_text
    "news_p": news_p.text
    "feature_image": feature_image
    "html_table": html_table
    "hemisphere_image_urls": hemisphere_image_urls
