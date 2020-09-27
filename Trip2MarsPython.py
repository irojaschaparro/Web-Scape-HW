from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def scrape_info():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    
    # 1 NASA Mars News

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    # 1 GOOD - NASA Mars News 
    headline = soup.find_all('div', class_ = 'content_title')
    paragraph = soup.find_all('div', class_ = 'article_teaser_body')
    news_title = headline[1].text
    news_p = paragraph[0].text

    print(news_p)
    
    # first_ex = {"News Header":news_title, "News Description":news_p}


    # 2 JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    img_url = soup.find(class_ = "button fancybox")["data-fancybox-href"]
    featured_image_url = "https://www.jpl.nasa.gov" + img_url
    featured_image_url


    # 3 Mars Facts
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    tables = pd.read_html(url)
    tables
    one_table = tables[0]
    one_table

    one_table = one_table.to_html()

    # third_ex = {"Table": one_table}


    # 4
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    Img_titles = []
    full_img_links = []

    Img_title = soup.find_all('h3')
    Img_title
    for title in Img_title:
        Img_titles.append(title.text)  
        
    Img_data = soup.find_all('a', class_ ='itemLink product-item')
    full_img_links = []
    for a in Img_data:
            if a['href'] not in full_img_links:
                full_img_links.append(a['href'])


    full_images = []
    sub_url = 'https://astrogeology.usgs.gov/'
    for partial_link in full_img_links:
        browser.visit(sub_url + partial_link)
        full_link = browser.links.find_by_text("Sample")["href"]
        full_images.append(full_link)


    # link_lists = [cer, sch, syr, val]

    dictionary = dict(zip(Img_titles, full_images))
    dictionary

    # fourth_ex = dict(zip(Img_titles, link_lists))
    # fourth_ex


    # Final - Accumulated list_dict
    # final = [first_ex, second_ex, third_ex, fourth_ex]
    # final = dict()

    final = {"News_Header":news_title, "News_Description":news_p, "Featured_Image": featured_image_url,
     "Table": one_table, "Links_and_Images": dictionary}


    browser.quit()

    return final