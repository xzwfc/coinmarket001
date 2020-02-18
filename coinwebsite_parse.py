

# f= open("coin1.html", 'r')
# html_content =f.read()
# print(html_content)

# f.close()


from bs4 import BeautifulSoup

f= open("coin1.html", 'r')
soup=BeautifulSoup(f.read(), "html.parser")

f.close()
# print (soup)
c_table=soup.find("table") #locate the content in the whole website
# print(c_table)

c_row=c_table.find("tr") #locate one row inside the table
# print (c_row)
c_b=c_row.find("td").find("a")
print(c_b)
# c_p=c_row.find("td",{"class":"hot_Num"}).find("a").text # a is the link From Tom's webpage

# print(c_p)
#td (class: ) is the column /td is the end of first column

#Class Feb 04
from bs4 import BeautifulSoup
# f= open("coin1.html", 'r')
# soup=BeautifulSoup(f.read(), "html.parser")
# f.close()

import os
if not os.path.exists ("parsed_files"):
	os.mkdir("parsed_files")

import pandas as pd
df=pd.DataFrame()

import glob
for one_file_name in glob.glob("try1/*.html"):
	
    scraping_time=os.path.basename(one_file_name).replace("blabal", "")
    f= open("one_file_name", 'r')
    soup=BeautifulSoup(f.read(), "html.parser")
    f.close()

# locate one by one
    currencies_table =soup.find("tbody")
    currencies_row =currencies_table.find("tr") #tr is the row
    currencies_price =currencies_row.find("td", {"class":"hot_Num"}).find("a", {"class":"cmc-link"}).text #class could help us locate by the name following it
    

# using loop for locating info from multiple rows
    currencies_table =soup.find("tbody")
    currencies_rows =currencies_table.find_all("tr")
    for r in currencies_rows:
	    currencies_price =r.find("td", {"class":"hot_Num"}).find("a", {"class":"cmc-link"}).text.replace(",", "")
	    currencies_market =r.find("td", {"class":"hot_Num2"}).find("a", {"class":"cmc-link2"}).text.replace(",", "")
	    currencies_link= r.find("td", {"class":"hot_Num2"}).find("a", {"class":"cmc-link2"})["href"]
	    print(currencies_price)
	    print(currencies_market)
        df=df.append({"time": scraping_time, "price":currencies_price, "market":currencies_market, "link":currencies_link}, ignore_index=True)

df.to_csv("parsed_files/dataset_names.csv")







