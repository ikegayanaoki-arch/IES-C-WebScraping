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


  ##ranking 
  #As of 2024/4/8 : <p class="sc-eLgNKc cpfgbD">
  lstPCl=soup.find_all("p", class_="sc-eLgNKc cpfgbD")
  #As of 2024/4/23 : <p class="sc-1t7ra5j-7 casbUp">
  #lstPCl=soup.find_all("p", class_="sc-1t7ra5j-7 casbUp")

  ##date & time stamp of ranking
  #As of 2024/4/8 : <span class="sc-hOqruk cNUsMV">4/6(土)</span>
  lstSpanCl=soup.find_all("span", class_="sc-hOqruk cNUsMV")
  #As of 2024/4/23 <span class="sc-1t7ra5j-10 cfHAOL">7:00</span>
  #lstSpanCl=soup.find_all("span", class_="sc-1t7ra5j-10 cfHAOL")

  for i in range(len(lstPCl)):
    j=i*2
    hl=lstPCl[i].string
    date=lstSpanCl[j].string
    time=lstSpanCl[j+1].string
    print(i, "\t", date, "\t", time, "\t", hl)

  #print("end of try")
##console output when error
except:
  print("error")


