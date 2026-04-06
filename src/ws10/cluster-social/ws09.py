##python3.9 #09 data load by pickle
import requests
from bs4 import BeautifulSoup   
import time   ##for time control
import pickle ##for data save by pickle (binary)
import matplotlib.pyplot as plt
import japanize_matplotlib
from wordcloud import WordCloud
import numpy as np
from PIL import Image

## try & error - main program
try:
  ## access "url" and get all html tags 
  #url="https://q-pit.kyushu-u.ac.jp/cluster-social/"
  #r = requests.get(url)
  #soup = BeautifulSoup(r.content, "html.parser")
  
  ##to restore data 
  opList=[]

  ##read pickled ata
  f=open("opList.dump", "rb")
  opList=pickle.load(f)
  ##for debugging
  #print(opList)
  
  ##dictionary type
  profData={'name':[], 'job title':[], 'affiliation':[], 'theme':[], 'keywords':[]}
  for op in opList: 
    profData['name'].append(op[0])
    profData['job title'].append(op[1])
    profData['affiliation'].append(op[2])
    profData['theme'].append(op[3])
    profData['keywords'].append(op[4])
    ## Ref: -- data order in opList
    #tmp=[]
    #tmp.append(name)   
    #tmp.append(jtl)   
    #tmp.append(afl)   
    #tmp.append(theme)   
    #tmp.append(key)   
    #opList.append(tmp)
  ##list key
  print(profData.keys()) 

  ##extract values in dictionary
  print(profData['name'])
  print(profData['job title'])

  ##loop by keys
  for key in profData.keys():
    print(key, profData[key])
    
  ##data analysis
  ##post-pro#1 frequency of job title
  fig=plt.figure()
  jbtList=profData['job title']
  catList=list(set(jbtList))
  data={}
  for cat in catList:
    data[cat]=jbtList.count(cat) 
  ##graph
  val=list(data.values())
  plt.bar(catList, val)
  plt.grid()
  plt.savefig("jtFreq.png")

  ## post-pro#2 frequency of affiliation 
  fig=plt.figure()
  tmpList=profData['affiliation']
  #aflList=[]
  aflList=[strn.split()[0] for strn in tmpList]
  catList=list(set(aflList))
  data={}
  for cat in catList:
    data[cat]=aflList.count(cat) 
  ##graph
  val=list(data.values())
  plt.bar(catList, val)
  plt.grid()
  plt.xticks(rotation=90)
  plt.savefig("aflFreq.png", bbox_inches='tight')

  ##Word could map
  words1=list(filter(None, profData['keywords']))
  words2=list(filter(None, profData['theme']))
  txt1=''.join(words1)
  txt2=''.join(words2)
  txt=txt1 + txt2
  ##for Japanese characters
  fp="/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"
  
  ##change shape for cloud
  #mask=np.array(Image.open("mask.png"))
  #mask=np.array(Image.open("mask2.png"))
  mask=np.array(Image.open("brain.png"))
  mask=255-mask ##nega-posi

  cmap="Paired"
  wc=WordCloud(
     stopwords=['の', '/',' ','(', ')', '・', '、', ', ', 'and', 'for', 'in', 'of '], 
     font_path=fp,
     background_color="white",
     colormap=cmap,
     width=800,
     height=800,
     mask=mask
     ).generate(txt)

  plt.figure(figsize=(10, 10))
  plt.imshow(wc, interpolation="bilinear")
  plt.axis("off")
  plt.savefig("wc.png")

  ##show graphs
  #plt.show() 
 
  #print("end of try")
##console output when error
except:
  print("error")


