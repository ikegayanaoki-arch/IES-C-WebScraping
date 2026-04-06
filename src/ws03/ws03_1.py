##python3.9 #03 html tag structure 
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access local html file
  file="./sampleTags.html" 
  soup = BeautifulSoup(open(file, encoding='utf-8'), "html.parser")

  ##find by tag: <a> and extract "string" and "href contents"
  print(" --- link tag --- ")
  lstA=soup.find_all("a")
  #lstA[0].string
  print(lstA[0].string)
  lstA[0].get("href")
  print(lstA[0].get("href"))
  
##console output when error
except:
  print("error")


