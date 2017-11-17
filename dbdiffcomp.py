
import sys
import sqlite3

if len(sys.argv) < 3:
  print ("USAGE: python3 dbdiffcomp.py <dbfile> <hashfile>")



right=open(sys.argv[2],"r")

con=sqlite3.connect(sys.argv[1])
left=con.cursor()

nextline=right.readline()
while nextline:
  nexthash=nextline.split("|")[1]
  left.execute("SELECT * from left where hash = '"+nexthash+"'")
  row=left.fetchone()
  if row == None:
    print("R|"+nextline.strip("\n"))
  else:
    print("L|"+str(row[0])+"-"+str(row[1])+"|"+row[2].strip("\n"))
  nextline=right.readline()
