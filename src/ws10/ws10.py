##python3.9 #08 figures & data save by pickle
import requests
from bs4 import BeautifulSoup   
import time   ##for time control
import pickle ##for data save by pickle (binary)
import sys ##for argument input

## try & error - main program
try:
  args = sys.argv
  clusterName=args[1]
  ## access "url" and get all html tags 
  urlBase="https://q-pit.kyushu-u.ac.jp/"
  url=urlBase+clusterName+"/"
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
  #for i in range(1): ##for debugging
    ##profile
    lstDt=lstDivClProf[i].find_all("dt") 
    lstDd=lstDivClProf[i].find_all("dd") 
    ##category and value
    cat=[j.string for j in lstDt] ##categories
    #val=[j.string.replace("\t", "") if (len(j) !=0) else j.string for j in lstDd] ## to avoid error 
    val=[j.text.replace("\t", "") if (len(j) !=0) else j.text for j in lstDd] 
    ##prof name
    #name=lstACl[i].string ##cause error when pickled
    name=str(lstACl[i].string )
    ##image file
    lstImg=lstDivCl[i].find_all("img", class_="attachment-full size-full wp-post-image")
    for j in range(len(lstImg)):
      ##url for image
      src=lstImg[j].get("src") 
      ##send requests to get image - for debug
      rImg=requests.get(src, allow_redirects=False)
      img=rImg.content
      ##save image
      ext=src.split(".")[-1]
      saveDir="./figs/"
      fn=saveDir + name + "." + ext
      f=open(fn, "wb")
      f.write(img)
      ##for debug
      #print(j, name, cat, val, src) 
      #time.sleep(1) # to recude access load
    ##if this data is new, store name, job title, affiliation, and keywords
    if name not in names: 
      names.append(name) #name list
      ##for debugging
      print(name, names)

      ##select output data 
      for k in range(len(cat)):
        print(k, val[k], cat[k])
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
  print(opList)
  f=open("opList.dump", "wb")
  pickle.dump(opList, f)

  #print("end of try")
##console output when error
except:
  print("error")


