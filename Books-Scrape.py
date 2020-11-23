from selenium import webdriver
import pandas as pd
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")

maxPage = 50
start = 1
alldetails = []
links = []

driver = webdriver.Firefox(options=options,executable_path="/home/faris/github/Python-Webscrape-Books/geckodriver")

for i in range(1,3):
    number = str(i)
    url = 'https://books.toscrape.com/catalogue/page-'+number+'.html'
    website = driver.get(url)


    thebooks=driver.find_elements_by_class_name("product_pod") # Contains all the product

    for book in thebooks:                                       # Links of product
        h3tag = book.find_elements_by_tag_name("h3")[-1]
        atag = h3tag.find_element_by_tag_name("a")
        links.append(atag.get_property('href'))

    for link in links:
        driver.get(link) #Product details
        nameofproduct = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1").text
        priceofproduct = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[1]").text
        available = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[2]").text
        details = {
        'Book Name' : nameofproduct,
        'Price': priceofproduct,
        'Instock' : available,
        'Link' : link
        }
        alldetails.append(details)

save = (pd.DataFrame(alldetails))
save.to_csv("results.csv")
