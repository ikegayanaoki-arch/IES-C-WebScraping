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
  
  ##main content button
  print(" -- main content button -- ")
  #As of 2024/4/23
  lstACl=soup.find_all("a", class_="sc-1mps4g6-0 gJIhOe")
  for i in range(len(lstACl)):
    cat=lstACl[i].string
    link=lstACl[i].get("href")
    if("https:" not in link): 
      link=urlBase + link
    print(cat, link)
  print("")

  #print("end of try")
##console output when error
except:
  print("error")


