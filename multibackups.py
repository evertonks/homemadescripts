#! /usr/bin/python3

import os

# diretorios.txt file example:
#  '/home/user/test/t1', '/home/user/backup/test'
#  '/home/user/test/t2', '/home/user/backup/test'

diretoriosTXT = open("diretorios.txt", "r")
array_list=[]

for row in diretoriosTXT:
  string_row = linha.strip()
  row_prow = string_row.split()
  array_list.append(row_prow)
  diretoriosTXT.close()  

for path_bkp in array_list:
  src = str(path_bkp[:1]).strip('[').strip(']').strip('"').strip(',')
  dest = str(path_bkp[1:2]).strip('[').strip(']').strip('"').strip(',')
  rsync = ('rsync -raAXtuv '+src+' '+dest)
  os.system(rsync)
