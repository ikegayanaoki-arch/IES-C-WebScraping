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
  lstDivId=soup.find_all("div", id="news_block")
  lstH3Cl=lstDivId[0].find_all("h3") 
  lstACl=lstDivId[0].find_all("a")
  lstTime=lstDivId[0].find_all("time")
  lstLi=lstDivId[0].find_all("li")

  for i in range(len(lstLi)):
    tH3Local=lstLi[i].find("h3")
    tTimeLocal=lstLi[i].find("time")
    lstH5Local=lstLi[i].find_all("h5")
    if(len(lstH5Local) != 0): 
      pi=[j.string for j in lstH5Local] ##personal information
      print(tTimeLocal.string)
      print("  ", tH3Local.string)
      print("    ", pi[0], pi[1])
      #print(i, tH3Local.string, tTimeLocal.string, pi)
    else : 
      pi=""

  #for i in range(len(lstH3Cl)):
  #  print(lstTime[i].string)
  #  print(lstH3Cl[i].string)
  #  news_url=lstACl[i].get("href")
  #  print(urlBase + news_url[1:])
 
  #print("end of try")
##console output when error
except:
  print("error")


