##python3.9 #03 html tag structure 
import requests
from bs4 import BeautifulSoup   

## try & error - main program
try:
  ## access local html file
  file="./sampleTags.html" 
  soup = BeautifulSoup(open(file, encoding='utf-8'), "html.parser")

  ##disply tags
  #print(soup)

  ##find by tag: <a> and extract "string" and "href contents"
  print(" --- link tag --- ")
  lstA=soup.find_all("a")
  #lstA[0].string
  print(lstA[0].string)
  lstA[0].get("href")
  print(lstA[0].get("href"))
  
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

  #print("end of try")
##console output when error
except:
  print("error")


