# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape() :
    browser = init_browser()
    # Create python dictionary to store return value in Mondodb 
    mars_data = {}
    
    ### NASA MARS NEWS

    # URL of page to scrape the latest news of Mars
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with splinter 
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Examine the results, get the latest news title and assingn it to the variable "news_title"
    news_title = soup.find(class_="bottom_gradient").get_text()

    # Collect the paragraph text of the latest Mars news and assing it to a variable "prg_text"
    prg_text = soup.find('div', class_="article_teaser_body").get_text()

    # Insert the news title and paragraph text to 'mars_data' dictionary
    mars_data['news_title'] = news_title
    mars_data['prg_text'] = prg_text

    ### JPL MARS SPACE IMAGES

    # Get the image url for the current featured mars image and assign the url string to a variable 
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" 
    browser.visit(jpl_url)

    # Create BeautifulSoup object and parse
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'lxml')

    # Find the url of featured image
    featured_image = jpl_soup.select('a.fancybox')
    images = [i.get('data-fancybox-href') for i in featured_image]
    images[1]
    
    # Put the base part of the webpage into a variable to combine with featured image url
    image_base_url = 'https://www.jpl.nasa.gov'

    # Combine the base url with the feauted image url
    featured_image_url = 'image_base_url' + images[1]
    
    # insert the url of featured image to mars_data dictionary
    mars_data['featured_image_url'] = featured_image_url
    
    ### MARS FACTS

    facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(facts_url)

    # Convert the table to a pandas dataframe
    facts_df = tables[0]
    
    # Convert the mars facts dataframe into a html table
    facts_html_table = facts_df.to_html(header=False, index=False)

    # Strip unwanted newlines to clean up the table
    facts_html_table = facts_html_table.replace('\n', '')
    
    # insert mars facts html table to mars_data dictionary
    mars_data['facts_html_table'] = facts_html_table

    ### MARS HEMISPHERES

    # Get high resolution images for each of Mars' hemispheres 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    # Create BeautifulSoup object and parse
    hemispheres_url_html = browser.html
    hemispheres_url_soup = BeautifulSoup(hemispheres_url_html, 'html.parser')

    #Find the image url of each hemispheres
    hemispheres = hemispheres_url_soup.select('div.item')


    hemisphere_image_urls = []

    for h in hemispheres:
        title = (h.find('h3').text).replace(' Enhanced', '')
        
         # click the hemisphere
        browser.click_link_by_partial_text(title)

         # make new soup of that page
        soup = BeautifulSoup(browser.html, 'html.parser')
    
         # find the full image
        full = soup.find('a', text='Sample')
    
         # get the img url
        img_url = full['href']
    
        # make a dictionary and append to the list
        hemisphere_image_urls.append({'title': title, 'img_url': img_url})
    
        # go back 
        browser.back()

    # close the browser
    browser.quit()    
    
    # insert hemispheres image urls to mars_data dictionary 
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    
    # retun results
    return mars_data