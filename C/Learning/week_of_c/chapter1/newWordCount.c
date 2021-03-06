#include <stdio.h>

#define IN 1 //inside a word
#define OUT 2 //outside a word


int main(){
  int c, nl, nw, nc, state;

  state = OUT;
  nl = nw = nc = 0;
  while((c = getchar()) != '\t'){//note that using tab in place of EOF
    ++nc;
    if(c == '\n'){
      ++nl;
    }
    if(c == ' ' || c == '\n' || c == '\t'){
      state = OUT;
    }
    else if(state == OUT){
      state = IN;
      ++nw;
    }
  }
  recurse(nl, nw, nc);
}

int recurse(int nl, int nw, int nc){
  printf("noOflines ==> %d, noOfWords ==> %d, noOfChars ==> %d\n", nl, nw, nc);
  main();
}

//end of code
