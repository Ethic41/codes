#include <stdio.h>
/*prinf fahrenheit-celius temperature values for 0,20,40...300*/

main(){
  int fahr, celcius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;

  while(fahr <= upper){
    celcius = 5 * (fahr - 32) / 9;
    printf("%3d\t%6d\n", celcius, fahr);
    fahr = fahr + step;
  }
}
