#include <stdio.h>


void function(){
  int var = 5;
  static int static_var = 5; //static variable initialization

  printf("\t[in function] var @ %p = %d\n", &var, var);
  printf("\t[in function] static_var @ %p = %d\n", &static_var, static_var);
  var++; //add 1 to var
  static_var++;//add 1 to static var
}

int main(){
  int i;
  static int static_var = 1337; //Another static, in a different context

  for(i=0; i < 5; i++){
    printf("[in main] static var @ %p = %d\n", &static_var, static_var);
    function(); // call funtion
  }
}

//end of code
