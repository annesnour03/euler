import time
def sol(grid):
    for i in range(len(grid) - 2,-1,-1):
        for j in range(len(grid[0]) - 1):
            grid[i][j] += max(grid[i + 1][j],grid[i + 1][j + 1])
    return grid[0][0]
def main():
    t0 = time.time()
    grid = []
    for i in open("18_input.txt","r"):
        i = i.rsplit()
        i  = [int(j) for j in i]
        grid.append(i)
    print(grid)
    print(sol(grid))
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()