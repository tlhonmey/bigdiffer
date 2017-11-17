#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[])
{

  if (argc != 2)
  {
    fprintf(stderr, "Usage: chunker <inputfile>");
    exit(1);
  }

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
	printf("%li\n",ftell(ifp));
	nulls=0;
      }
    }
    else
    {
      nulls=0;
    }

  
    value = fgetc(ifp);

  }
  fclose(ifp);

}
