import hashlib
import sys

if len(sys.argv)<4:
  print("Usage: hasher.py <sourcefile> <chunklist> <hashfile>") 
  exit(1)

f=open(sys.argv[1],"rb")
splits=["0\n"]+open(sys.argv[2],"r", encoding=sys.stdout.encoding ).readlines()
o=open(sys.argv[3],"wb")

for i in range(0,len(splits)-1):
  f.seek(int(splits[i]))
  o.write(splits[i].strip("\n").encode(sys.stdout.encoding))
  o.write("-".encode(sys.stdout.encoding))
  o.write(splits[i+1].strip("\n").encode(sys.stdout.encoding))
  o.write("|".encode(sys.stdout.encoding))
  o.write(hashlib.md5(f.read(int(splits[i+1])-int(splits[i]))).hexdigest().encode(sys.stdout.encoding))
  o.write("\n".encode(sys.stdout.encoding))


tail=f.read()
o.write(splits[-1].strip("\n").encode(sys.stdout.encoding))
o.write("-".encode(sys.stdout.encoding))
o.write(str(f.tell()).encode(sys.stdout.encoding))
o.write("|".encode(sys.stdout.encoding))
o.write(hashlib.md5(tail).hexdigest().encode(sys.stdout.encoding))

  
