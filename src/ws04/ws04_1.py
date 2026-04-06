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
  
  ##disply tags
  #print(soup)

  ##need to expalin how to built this code --> Excersize
  ##重要なお知らせ -- id="caution_block"
  print(" --- caution_block --- ")
  lstDivId=soup.find_all("div", id="caution_block")
  lstH3=lstDivId[0].find_all("h3")
  for i in range(len(lstH3)):
    print(i, lstH3[i].string)

  #print("end of try")
##console output when error
except:
  print("error")


