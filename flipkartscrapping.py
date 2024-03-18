import requests
import pandas as pd
from bs4 import BeautifulSoup
proname=[]
price=[]
des=[]
rev=[]
user_agent = 'Chrome/117.0.0.0' #CHANGING THE USER AGENT CAN HELP TO REISTABLISH THE CONNECTION TO THE SERVER

headers = {'User-Agent': user_agent}
for i in range (2,12): # LOOP FOR ITRATING TO THE NEXT PAGES OF THE SITE
    r = requests.get(
        "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=" + str(i),
        headers=headers) # GETTING THE HTML FROM THE LINK AND SAVING IN VARIABLE R

    html = r.text # SAVING THE HTML TEXT IN A VARIBLE FOR FURTHER PROCESSING
    # print(resp)
    soup = BeautifulSoup(html, 'lxml') # PASSING THE HTML TEXT IN THE BEAUTIFULSOUP FUNCION  WITH A PARSER LXML AND HTML.PARSER CAN BE USED FOR THE LESS COMPLEX HTMLS
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg") # SELCTING THE AREA FROM WHERE DATA HAS TO BE SCRAPED
    names = box.find_all("div", class_="_4rR01T") # EXTRACTING THE PRODUCT NAMES
    for i in names:# LOOPING THE NAMES LIST FOR DATA CLEARING
        name = i.text #DATA CLEARING
        proname.append(name)# AFTER REMOVING THE NOICE ADDING DATA INTO THE FRESH DATA LIST
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")# EXTRACTING PRICES
    for j in prices:# LOOP FOR DATA CLEARING
        pr = j.text
        price.append(pr)
    description = box.find_all("li", class_="rgWa7D")# EXTRACTING DESCRIPTION
    for i in description:
        name = i.text
        des.append(name)
    revivew = box.find_all("div", class_="_3LWZlK") #EXTRACTING REVIEWS
    for i in revivew:
        rw = i.text
        rev.append(rw)
df = pd.DataFrame({"pro name ": proname, "price": price, "rev": rev}) #MAKING DATAFRAME
print(df)
# PRINTING DATA FRAME