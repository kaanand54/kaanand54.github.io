# Run this script on ubuntu

#!/usr/bin/python
#!/bin/bash
import os
# prerequisites
# install mysql
# create a database db and a table 'products' inside db
# import dataset in 'products'
#create a mysql user and grant  only select privilege
#install shellinabox
user=raw_input("Enter mysql user:" )
password=raw_input("Enter password:")
while True:
  sql=raw_input("Sql$ ")
  if sql=='exit':
    exit()
  cmd="echo '"+sql+"' | mysql --user=user --password=password db"
  os.system(cmd)
  print("\n\n")
