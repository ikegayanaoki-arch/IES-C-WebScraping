##python3.9 #02 html tag structure 
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access "url" and get all html tags 
  #url="https://www.kyushu-u.ac.jp/ja/"
  #r = requests.get(url)
  #soup = BeautifulSoup(r.content, "html.parser")
  file="./sampleTags.html" 
  soup = BeautifulSoup(open(file, encoding='utf-8'), "html.parser")

  ##disply tags
  #print(soup)

  ##find by tag: <body>
  tBody=soup.find("body") #tag by <body>
  lstBody=soup.find_all("body") #tag list by <body>

  ##find by tag: <a>
  tA=soup.find("a")
  lstA=soup.find_all("a")
  
  ##find by tag and class or id :<div class=>/<div id=>
  lstDiv=soup.find_all("div")
  #lstDiv
  lstDivId=soup.find_all("div", id="stitle")
  #lstDivId
  lstDivCl=soup.find_all("div", class_="dummy")
  #lstDivCl

  print("end of try")
##console output when error
except:
  print("error")


