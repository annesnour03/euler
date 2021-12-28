#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *find(int range, int maal) {
  int *arr = calloc(1, 10000);
  for (int i = 0; i < range; i++) {
    int number = i * maal;

    if (number > range  - 1) break;
    arr[i] = number;
  }
  return arr;
}

int calc_sum(int *three, int range) {
  int total = 0;
  for (int i = 0; i <= range; i++) {
    total += three[i];
      printf("three post %d  total %d\n",three[i],total);
  }
  return total;
}

int main(void) {
  int max = 1000;
  int *array = find(max, 3);
  int *array_five = find(max, 5);
  int *array_15 = find(max, 15);

  int sum_three = calc_sum(array,max);
  int sum_five = calc_sum(array_five,max);
  int sum_15 = calc_sum(array_15,max);

  printf("sum %d\n", sum_three + sum_five - sum_15);

  free(array);
  free(array_five);

  return 0;
} 

// 266333 wrong