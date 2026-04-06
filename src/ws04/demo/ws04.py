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

  ##NEWS -- news_block 
  print(" --- news_block --- ")
  #lstDivId=soup.find("div", id="news_block")
  lstDivId=soup.find_all("div", id="news_block")
  lstH3Cl=lstDivId[0].find_all("h3", class_="a_new") 
  lstTime=lstDivId[0].find_all("time")
  lstACl=lstDivId[0].find_all("a", class_="a_new")
  for i in range(len(lstH3Cl)):
    print(lstTime[i].string)
    print(lstH3Cl[i].string)
    news_url=lstACl[i].get("href")
    print(urlBase + news_url[1:])
 
  ##FAST FACTS 数字で見る九州大学 -- facts_block
  print(" --- facts_block --- ")
  tDivId=soup.find("div", id="facts_block") 
  tUlCl=tDivId.find("ul", class_="body")
  lstP=tUlCl.find_all("p")
  lstH3=tUlCl.find_all("h3")
  for i in range(len(lstP)):
    cat=lstH3[i].contents[0]
    num=int(lstP[i].string.replace(",", ""))
    print(cat, num)
     
  ##ALL** --btn_block 
  print(" --- btn_block --- ")
  lstACl=soup.find_all("a", class_="btn_block") 
  lstLink=[] 
  lstTl=[] 
  for i in range(len(lstACl)):
    tl=lstACl[i].string
    lk=lstACl[i].get("href")
    link=urlBase + lk[1:]
    #print(i,tl, link)
    if(tl not in lstTl):
      lstLink.append(link)
      lstTl.append(tl)
  for i in range(len(lstTl)):
    print(i, lstTl[i], lstLink[i])
    
  #print("end of try")
##console output when error
except:
  print("error")


