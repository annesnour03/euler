#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool check_if_prime(long long n) {
  if (n <= 1) return false;

  for (long long i = 2; i < n; i++) {
    if (!(n % i)) return false;
  }
  return true;
}

void primes_calc(long long* primes, long long range) {
  long long counter = 0, i = 0;
  while (1) {
    if (check_if_prime(i)) {
      printf("i =  %d\n", i);
      primes[counter++] = i;
    }
    if (counter >= range) break;
    i++;
  }
  return;
}

int main(void) {
  int i = 10001;
  long long* primes = calloc(1, 100000 * sizeof(int));
  if (!primes) exit(1);

  printf("%d\n", primes[i - 1]);
  return 0;
}