#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>



int tnum(int x) { return ((x * x + x) / 2); }
int num_div(int x) {
  int counter = 1;
  for (int i = 1; i < sqrt(x) + 1; i++) {
    if (!(x % i)) counter++;
  }
  return counter;
}
int main(void) {
        time_t before = time(NULL);

  for (int i = 0; i < INT_MAX; i++) {
    if (num_div(tnum(i)) >= 150) {
      printf("%d\n", i);

      break;
    }
  }
      double difference = difftime(time(NULL), before);
    printf("The time taken was %lf seconds.\n", difference);

}