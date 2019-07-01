#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[])
{

  if (argc != 2)
  {
    fprintf(stderr, "Usage: chunker <inputfile>");
    exit(1);
  }
  const int MAX_CHUNK_SIZE=1024*1024; /* 1MB */
  const int RH_LENGTH=8;
  unsigned int rhData[RH_LENGTH];
  unsigned int bytecount=0;
  char * mode = "r";
  FILE * ifp;
  int nulls=0;
  unsigned char value='\0';

  ifp = fopen (argv[1], mode);
  if (ifp == 0x00)
  {
    fprintf(stderr, "Can't open input file\n");
    exit(1);
  }


  value = fgetc(ifp);

  while (! feof(ifp) )
  {
    if (value == 0x00)
    {
      nulls++;
      if (nulls >= 16)
      {
        goto printchunk;
      }
    }
    else
    {
      nulls=0;
    }
    if (bytecount > MAX_CHUNK_SIZE) 
    {
      goto printchunk;
    }
    rhData[bytecount % RH_LENGTH]=value;
    if (bytecount > RH_LENGTH)
    {
      unsigned int sum=0;
      for (int i=0; i<RH_LENGTH; i++)
      {
        sum += rhData[i];
      }
      sum /= RH_LENGTH;
      if (sum > 120 && sum < 130)
      {
        goto printchunk;
      }
    }
  
    bytecount+=1;
    value = fgetc(ifp);
    continue;
printchunk:
    printf("%li\n",ftell(ifp));
    nulls=0;
    bytecount=0;
    value = fgetc(ifp);

  }
  fclose(ifp);

}
