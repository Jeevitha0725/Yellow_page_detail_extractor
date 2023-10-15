from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

driver=webdriver.Chrome()
# niche=input("Enter your niche...? ")
# location=input("Enter your location: ")
# driver.get(f'http://yellowpages.in/{location}/{niche}/606286653')
driver.get('http://yellowpages.in/hyderabad/food-and-beverages/606286653')
time.sleep(5)
soup=BeautifulSoup(driver.page_source,"html.parser")
con=soup.find("ul",attrs={"class","popularThisWeekList"})

Y_page={"Name":[],"Link":[],"Phone Number":[],"Address":[],"Reviews":[],"Opens Till":[]}
for i in con:
    print(i)
    link=i.find("a",class_='eachPopularTitle hasOtherInfo').get("href")
    Link=f"http://yellowpages.in{link}"
    name=i.find("a",class_='eachPopularTitle hasOtherInfo').text
    Phone_No=i.find("a",class_='businessContact').text
    Address=i.find("address",class_='businessArea').text
    Reviews=i.find("a",class_='ratingCount').text
    Opening_Time=i.find("div",class_='openNow').text
    Y_page["Name"].append(name)
    Y_page["Link"].append(Link)
    Y_page["Phone Number"].append(Phone_No)
    Y_page["Address"].append(Address)
    Y_page["Reviews"].append(Reviews)
    Y_page["Opens Till"].append(Opening_Time)
Dataframe=pd.DataFrame.from_dict(Y_page)
Dataframe.to_csv(r"C:\Users\sjeev\Documents\Python\Web_scraping\Yellow_page_details.csv",index=True)
print(Dataframe)
