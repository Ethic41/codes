#include <stdio.h>

main(){
  //program counts characters
  long nc;

  nc = 0;

  while((getchar() != EOF)){
    ++nc;
    printf("%ld\n", nc);
  }
}
