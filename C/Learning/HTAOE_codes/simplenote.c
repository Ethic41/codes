#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>


void usage(char *prog_name, char *filename){
  printf("Usage: %s <data to add to %s>\n", prog_name, filename);
  exit(0)
}

void fatal(char *); //a function for fatal errors
void *ec_malloc(unsigned int); // an error checked malloc() wrapper

int main(int argc, char *argv[]){
  int fd; //file discriptor
  char *buffer, *datafile;

  buffer = (char *) ec_malloc(100);
  datafile = (char *) ec_malloc(20);
  strcpy(datafile, "/tmp/notes");

  if(argc < 2){
    usage(argv[0], datafile);
  }
}


//end of code
