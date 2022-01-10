#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned fibonacci(long long begin) {
  if (begin <= 1) return begin;

  return fibonacci(begin - 1) + fibonacci(begin - 2);
}

int main(void) {
  int max = 100;
  long long all[max];

  for (int i = 1; i < max; i++) {
    long long fibo = fibonacci(i);
    if (fibo > 4e6) {
      break;
    }
    all[i] = fibo;
  }

  int total = 0;
  for (int i = 1; i < max; i++) {
    if (all[i] > 4e6) break;
    if (!(all[i] % 2)) {
      total += all[i];
    }
  }
  printf("total = %d\n", total);

  return 0;
}