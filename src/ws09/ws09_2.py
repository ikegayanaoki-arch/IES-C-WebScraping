##python3.9 #09 data load by pickle
import requests
from bs4 import BeautifulSoup   
import pickle ##for data save by pickle (binary)
import matplotlib.pyplot as plt
import japanize_matplotlib
from wordcloud import WordCloud
import numpy as np
from PIL import Image
## try & error - main program
try:
  ##to restore data 
  opList=[]

  ##read pickled ata
  f=open("opList.dump", "rb")
  opList=pickle.load(f)
  ##for debugging
  print(opList)
  
  ##dictionary type
  profData={'name':[], 'job title':[], 'affiliation':[], 'theme':[], 'keywords':[]}
  for op in opList: 
    profData['name'].append(op[0])
    profData['job title'].append(op[1])
    profData['affiliation'].append(op[2])
    profData['theme'].append(op[3])
    profData['keywords'].append(op[4])
  ##list key
  print(profData.keys()) 

  ##extract values in dictionary
  print(profData['name'])
  print(profData['job title'])

  ##loop by keys
  for key in profData.keys():
    print(key, profData[key])
    
  ##Word could map
  words1=list(filter(None, profData['keywords']))
  words2=list(filter(None, profData['theme']))
  txt1=''.join(words1)
  txt2=''.join(words2)
  txt=txt1 + txt2
  ##for Japanese characters
  fp="/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"
  
  ##change shape for cloud
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
  plt.show() 
 
  #print("end of try")
##console output when error
except:
  print("error")


