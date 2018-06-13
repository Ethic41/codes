#include <stdio.h>
#include <makeWordHistogram.h>

int makeWordHistogram(int);

int main(){
  int c, count, starting, lastChar;

  count = 0;
  starting = 1;
  while((c = getchar()) != EOF){
    if(c == ' ' || c == '\t' || c == '\n'){
      if(starting == 1){
        ;
      }
      else if(lastChar != ' ' && lastChar != '\t' && lastChar != '\n'){
        makeWordHistogram(count);
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

//end of code
