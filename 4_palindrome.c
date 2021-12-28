#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "stack.h"

bool check_if_palindromic(int i) {
  char *c = malloc(1000);
  itoa(i, c, 10);
  size_t len = strlen(c);
  int counter = 0;

  for (int i = 0; i < len; i++) {
    if ((c[len - i - 1] == c[i])) {
      counter++;
    } else {
      break;
    }
  }
  free(c);
  if (counter == len) return true;
  return false;
}
int main(void) {
  int max = -__INT_MAX__;
  int range = 999;

  for (int i = 0; i < range; i++) {
    for (int j = 0; j < range; j++) {
      if (check_if_palindromic(i * j)) {
        if (i * j > max) max = i * j;
      }
    }
  }

  printf("max = %d\n", max);
  return 0;
}