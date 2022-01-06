#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool even_divisible(int num, int range) {
  int counter = 0;
  for (int i = 1; i <= range; i++) {
    if (!(num % i)) counter++;
  }
  return counter == range ? true : false;
}

int main(void) {
  for (int i = 1; i < INT_MAX; i++) {
    if (even_divisible(i, 20)) {
      printf("%d\n", i);
      break;
    }
  }

  return 0;
}