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
  
  ##ranking 
  #As of 2024/4/23 : <p class="sc-1t7ra5j-7 casbUp">
  lstPCl=soup.find_all("p", class_="sc-1t7ra5j-7 casbUp")

  ##date & time stamp of ranking
  #As of 2024/4/23 <span class="sc-1t7ra5j-10 cfHAOL">7:00</span>
  lstSpanCl=soup.find_all("span", class_="sc-1t7ra5j-10 cfHAOL")

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


