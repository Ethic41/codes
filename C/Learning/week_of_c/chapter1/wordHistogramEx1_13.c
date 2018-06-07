#include <stdio.h>


int main(){
  int c, count, starting, lastChar;

  count = 0;
  starting = 1;
  while((c = getchar()) != '\t'){
    if(c == ' ' || c == '\t' || c == '\n'){
      if(starting == 1){
        ;
      }
      else if(lastChar != ' ' && lastChar != '\t' && lastChar != '\n'){
        makeHistogram(count);
        count = 0;
        lastChar = c;
      }
    }
    else if(c){
      ++count;
      starting = 0;
      lastChar = c;
    }
  }
}

int makeHistogram(int length){
  int i;

  for(i=0; i < length; i++){
    printf("====");
  }
  printf("\n%d", length);
  //printf("\n%d", length);
  for(i=0; i < length; i++){
    printf("    ");
  }
  if(length < 10){
    printf("\b\b|\n");
  }
  else{
    printf("\b\b\b|\n");
  }
  for(i=0; i < length; i++){
    printf("====");
  }
  printf("\n");

}

//end of code
