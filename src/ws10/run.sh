#!/bin/bash

 ##using argument of program
 ##access three cluster
 CLIST="cluster-material cluster-system cluster-social"
  
 for c in $CLIST
 do
   if [ -e $c  ]  
   then
     rm -rf $c
   fi 
   mkdir figs
   python3.9 ws10.py $c 
   mv figs $c 
   mv opList.dump $c

 done
 


