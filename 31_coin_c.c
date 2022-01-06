#include <stdio.h>
#include <stdlib.h>
int coins[] = {1,2,5,10,20,50,100,200};
void print_arr(int **grid, int y, int x) {
  for (int i = 0; i < y; i++) {
    for (int j = 0; j < x; j++) {
      printf("%d ", grid[i][j]);
    }
    printf("\n");
  }
}

int solve(int amount_coins, int sum) {
  int **grid = calloc(1, (amount_coins + 1) * (++sum + 1) * sizeof(int));
  for (int i = 0; i < amount_coins; i++) {
    grid[i] = calloc(1, 1000);
  }
  
  // First row filled with 1's
  for (int i = 0; i < amount_coins; i++) {
    grid[i][0] = 1;
  }

  // Logic
  for (int i = 0; i < amount_coins; i++) {
    for (int j = 1; j <= sum; j++) {
      int with = 0;
      int without = 0;
      if (j - coins[i] >= 0){
          with = grid[i][j-coins[i]];
      }
      if(i > 0){
          without = grid[i- 1][j];
      }

      grid[i][j] =  with + without;
    }
  }
  print_arr(grid, amount_coins, sum);

  return grid[amount_coins - 1][sum - 1];
}

int main(void) {
    int size = sizeof(coins) / sizeof(coins[0]);
  printf("%d ", solve(size,200));
  return 0;
}