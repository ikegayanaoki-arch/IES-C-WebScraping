##python3.9 #05 Yahoo News
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access "url" and get all html tags 
  urlBase="https://news.yahoo.co.jp"
  url=urlBase
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser")
  
  ##topics
  print(" -- topics -- ")
  #As of 2024/4/23
  lstACl=soup.find_all("a", class_="sc-1nhdoj2-1 hKGArG")
  for i in range(len(lstACl)):
    cat=lstACl[i].contents[0]
    link=lstACl[i].get("href")
    if("https:" not in link): 
      link=urlBase + link
    print(cat, link)

  #print("end of try")
##console output when error
except:
  print("error")


