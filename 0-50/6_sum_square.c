#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int square_sum(int range, int flip) {
  int res = 0;
  for (int i = 0; i <= range; i++) {
    res = (flip == 1) ? res + i : res + i*i;
  }
  return res;
}
int main(void) {
  int range = 100;
  printf("res = %d\n", square_sum(range,1) *  square_sum(range,1) - square_sum(range,0));

  return 0;
}