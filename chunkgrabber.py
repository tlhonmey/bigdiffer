import sys

if len(sys.argv)<4:
  print("USAGE: python3 chunkgrabber.py <destfile> <chunklist> <patchdata>")


r=open(sys.argv[1],"rb")
o=open(sys.argv[3],"wb+")
d=open(sys.argv[2],"r")


l=d.readline()

while l:
  sections=l.split("|")
  if sections[0]=="R":
    field=sections[1].split("-")
    r.seek(int(field[0]))
    o.seek(int(field[0]))
    o.write(r.read(int(field[1])-int(field[0])))
  l=d.readline()


