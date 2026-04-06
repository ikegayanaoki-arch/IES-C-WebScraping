##python3.9 #03 html tag structure 
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access local html file
  file="./sampleTags.html" 
  soup = BeautifulSoup(open(file, encoding='utf-8'), "html.parser")

  ##find by tag and class or id :<div class=>/<div id=>
  print(" --- div tag --- ")
  lstDivId=soup.find_all("div", id="stitle")
  ##multiple contents in lstDivId 
  for i in range(len(lstDivId)):
    #lstDivId[i].string
    print(i, lstDivId[i].string)
 
  ##find by tag <td> 
  print(" --- td tag --- ")
  lstTd=soup.find_all("td")
  for i in range(len(lstTd)):
    print(i, lstTd[i].string) 

##console output when error
except:
  print("error")


