#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>


int main(){
  printf("real uid: %d\n", getuid());
  printf("effective uid: %d\n", geteuid());
}

//end of code
