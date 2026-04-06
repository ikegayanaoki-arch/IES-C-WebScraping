##python3.9 #07 figures with labels
import requests
from bs4 import BeautifulSoup   
import time   ##for time control

## try & error - main program
try:
  ## access "url" and get all html tags 
  url="https://q-pit.kyushu-u.ac.jp/cluster-social/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, "html.parser")
  
  ##disply tags
  #print(soup)

  ##save figures with name
  lstDivCl=soup.find_all("div", class_="teacher_list_item") # category
  lstACl=soup.find_all("a", class_="fs_xxl") # name
  for i in range(len(lstDivCl)):
    ##prof name
    name=lstACl[i].string
    ##image file
    lstImg=lstDivCl[i].find_all("img", class_="attachment-full size-full wp-post-image")
    for j in range(len(lstImg)):
      ##url for image
      src=lstImg[j].get("src") 
      ##send requests to get image
      rImg=requests.get(src, allow_redirects=False)
      img=rImg.content
      ##save image
      ext=src.split(".")[-1]
      saveDir="./figs/"
      fn=saveDir + name + "." + ext
      f=open(fn, "wb")
      f.write(img)
      ##for debug
      print(j, name, src) 
      time.sleep(1)  ## to reduce access load

  #print("end of try")
##console output when error
except:
  print("error")


