

import sqlite3
import sys

if len(sys.argv) <3:
  print ("USAGE: python dbloader.py <hashfile> <databasefile>")
  exit(1)

f=open(sys.argv[1],"r")
con=sqlite3.connect(sys.argv[2])

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS left")
cur.execute("CREATE TABLE left(start INT, stop INT, hash TEXT)")


v=f.readline()
while v:
  s=v.split("|")
  hash=s[1]
  s=s[0].split("-")
  start=s[0]
  stop=s[1]
  cur.execute("INSERT INTO left VALUES("+start+","+stop+",'"+hash+"')")
  v=f.readline()

con.commit()
cur.execute("create index if not exists idx1 on left(hash)")
con.commit()
