n = int(input())
j = 1
k = n - 1

for i in range(n, 0, -1):
    print("  "*(i-1) + "* " * j + "* " * (j-1))
    j+=1

for i in range(1, j):
    print("  " * i + "* " * k + "* " * (k-1))
    k-=1



"""
                      *
                    * * *
                  * * * * *
                * * * * * * *
                  * * * * *
                    * * *
                      *
"""