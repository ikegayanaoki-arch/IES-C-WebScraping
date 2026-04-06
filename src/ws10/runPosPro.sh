#!/bin/bash

 ##using argument of program
 ##access three cluster
 CLIST="cluster-material cluster-system cluster-social"
  
 for c in $CLIST
 do
   #if [ -e $c  ]  
   #then
   #  rm -rf $c
   #fi 

   #mkdir figs
   cp ws09.py brain.png htmlIndex.sh $c
   cd $c
     python3.9 ws09.py $c 
     rm brain.png
     ./htmlIndex.sh 
     cp wc.png ../${c}.png
   cd ..
   #mv figs $c 
   #mv opList.dump $c

 done
 
 ./htmlIndex.sh 
 


