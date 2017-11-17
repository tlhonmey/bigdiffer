

import sys

if len(sys.argv)<5:
  print("USAGE: patcher.py <originalfile> <datafile> <controlfile> <output>")
  exit(1)


l=open(sys.argv[1],"rb")
r=open(sys.argv[2],"rb")
d=open(sys.argv[3],"r")
o=open(sys.argv[4],"wb")

v=d.readline()
while v:
  fields=v.split("|")
  chunk=fields[1].split("-")
  if fields[0]=="L":
    l.seek(int(chunk[0]))
    o.write(l.read(int(chunk[1])-int(chunk[0])))
  elif fields[0]=="R":
    r.seek(int(chunk[0]))
    o.write(r.read(int(chunk[1])-int(chunk[0])))
  else:
    print("ERROR, corrupted diff file")
  v=d.readline()

o.close()
