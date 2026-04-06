##python3.9 #04 Kyushu University website
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access "url" and get all html tags 
  urlBase="https://www.kyushu-u.ac.jp/"
  url=urlBase + "ja/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser")
  
  ##NEWS -- news_block 
  print(" --- news_block --- ")
  #lstDivId=soup.find("div", id="news_block")
  lstDivId=soup.find_all("div", id="news_block")
  lstH3Cl=lstDivId[0].find_all("h3") 
  lstACl=lstDivId[0].find_all("a")
  lstTime=lstDivId[0].find_all("time")

  #print("end of try")
##console output when error
except:
  print("error")


