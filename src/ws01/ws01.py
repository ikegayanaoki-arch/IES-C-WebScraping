##python3.9 #01 access
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ##url to access 
  url="https://www.kyushu-u.ac.jp/ja/"
  url="https://news.yahoo.co.jp"
  #url="https://www.tj.kyushu-u.ac.jp"

  ## access "url" and get all html tags 
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser")
  
  ##disply tags
  print(soup)

  print("end of try")
##console output when error
except:
  print("error")


