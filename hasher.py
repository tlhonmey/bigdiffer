import hashlib
import sys

if len(sys.argv)<4:
  print("Usage: hasher.py <sourcefile> <chunklist> <hashfile>") 
  exit(1)

f=open(sys.argv[1],"rb")
splits=["0\n"]+open(sys.argv[2],"r").readlines()
o=open(sys.argv[3],"wb")

for i in range(0,len(splits)-1):
  f.seek(int(splits[i]))
  o.write(splits[i].strip("\n"))
  o.write("-")
  o.write(splits[i+1].strip("\n"))
  o.write("|")
  o.write(hashlib.md5(f.read(int(splits[i+1])-int(splits[i]))).hexdigest())
  o.write("\n")


tail=f.read()
o.write(splits[-1].strip("\n"))
o.write("-")
o.write(str(f.tell()))
o.write("|")
o.write(hashlib.md5(tail).hexdigest())

  
