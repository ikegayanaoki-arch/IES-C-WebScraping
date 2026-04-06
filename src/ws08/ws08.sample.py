##python3.9 #08 figures & data save by pickle
import requests
from bs4 import BeautifulSoup   
import time   ##for time control
import pickle ##for data save by pickle (binary)

## try & error - main program
try:
  ## access "url" and get all html tags 
  url="https://q-pit.kyushu-u.ac.jp/cluster-social/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser")
  
  ##disply tags
  #print(soup)

  ##to store data - list and dump
  opList=[]
  names=[] #name -- for chekcing overlap

  ##save figures with name
  lstDivCl=soup.find_all("div", class_="teacher_list_item") # category
  lstACl=soup.find_all("a", class_="fs_xxl") # name
  lstDivClProf=soup.find_all("div", class_="teacher_list_item_profile") # profile
  for i in range(len(lstDivCl)):
    ##profile
    lstDt=lstDivClProf[i].find_all("dt") 
    lstDd=lstDivClProf[i].find_all("dd") 
    ##category and value
    cat=[j.string for j in lstDt] ##categories
    val=[j.string.replace("\t", "") if (len(j) !=0) else j.string for j in lstDd] 

    ##prof name
    #name=lstACl[i].string ##cause error when pickled
    name=str(lstACl[i].string )
    if name not in names: 
      names.append(name) #name list
      ##for debugging
      #print(name, names)
      print(name)

      ##select output data 
      for k in range(len(cat)):
        #print(k, val[k], cat[k])
        if(cat[k] == "職位") : jtl=val[k]
        if(cat[k] == "所属") : afl=val[k]
        if(cat[k] == "研究テーマ") : theme=val[k]
        if(cat[k] == "キーワード") : key=val[k]

      ##for pickle output - in the order output
      tmp=[]
      tmp.append(name)   
      tmp.append(jtl)   
      tmp.append(afl)   
      tmp.append(theme)   
      tmp.append(key)   
      ## append in output list
      opList.append(tmp)
      ##for debugging
      #print(opList)

  ##pickled 
  ##for debugging
  #print(opList)
  f=open("opList.dump", "wb")
  pickle.dump(opList, f)

  #print("end of try")
##console output when error
except:
  print("error")


