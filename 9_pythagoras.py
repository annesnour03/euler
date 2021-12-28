
def main():
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if (i *i + j* j) == k*k and i + j + k == 1000:
                        print("values",i * j *k)
    
if __name__ == "__main__":
    main()
