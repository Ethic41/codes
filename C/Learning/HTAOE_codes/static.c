#include <stdio.h>


void function(){
  int var = 5;
  static int static_var = 5; //static variable initialization

  printf("\t[in function] var = %d\n", var);
  printf("\t[in function] static_var = %d\n", static_var);
  var++; //add one to var.
  static_var++; //add one to static_var.
}

int main(){
  int i;
  static int static_var = 1337; //Another static variable

  for(i=0; i < 5; i++){
    printf("[in main] static var = %d\n", static_var);
    function(); //call the function
  }
}

//end of code
