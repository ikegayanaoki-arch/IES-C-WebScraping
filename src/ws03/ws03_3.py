##python3.9 #03 html tag structure 
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access local html file
  file="./sampleTags.html" 
  soup = BeautifulSoup(open(file, encoding='utf-8'), "html.parser")

  ##find by tag <tr>, extract contents as list
  print(" --- tr tag --- ")
  lstTr=soup.find_all("tr")
  for i in range(len(lstTr)):
    print(i, lstTr[i].contents) 

  ##extract component from list - double loop
  for i in range(len(lstTr)):
    print(i, lstTr[i].contents) 
    for j in range(len(lstTr[i].contents)):
      print(i,j, lstTr[i].contents[j].string)
      print(i,j, lstTr[i].contents[j].contents)

##console output when error
except:
  print("error")


