#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool check_if_prime(long long  n) {
  if (n <= 1) return false;

  for (long long i = 2; i < n; i++) {
    if (!(n % i)) return false;
  }
  return true;
}

void primes_calc(long long* primes, long long range) {
  long long counter = 0;
  for (long long i = 0; i < range; i++) {
    if (check_if_prime(i)) primes[counter++] = i;
  }

  return;
}

void print(long long* p, long long max) {
  for (long long i = 0; i < max; i++) {
    printf("%d ", p[i]);
  }
}

long long* get_factors(long long* primes, long long calc, long long max) {
  long long* factors = calloc(1, max * sizeof(long long));
  long long counter = 0;
  for (long long i = 0; i < calc; i++) {
    while (!(calc % primes[i])) {
      calc /= primes[i];
      factors[counter++] = primes[i];
    }
  }
  return factors;
}

int main(void) {
  long long max = 100000;
  long long num_to_calc = 600851475143;
  long long* primes = calloc(1, max * sizeof(long long));
  primes_calc(primes, max);

  long long* factors = get_factors(primes, num_to_calc, max);
  print(factors, 20);

  free(primes);
  free(factors);
  return 0;
}