# this is after the parsing step
import urllib.request
import os
import pandas as pd
import time

if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")

df= pd.read_csv("deep_link_html/coindataset_names.csv")

for link in df["link"]:
	filename=link.replace("/","").replace("curriencies","")
    if not os.path.exists("deep_link_html/" + filename+".html"):
    	print(filename+"exists")
    else:
    	f=open("deep_link_html/" + filename+".html.temp","wb")
	    response = urllib.request.urlopen('https://coinmarketcap.com/')
	    html =response.read()
	    f.write(html)
	    f.close()
	    os.rename("deep_link_html/" + filename+".html.temp","deep_link_html/" + filename+".html")
	    time.sleep(20)
	    # print ("https://coinmarketcap.com"+link)
