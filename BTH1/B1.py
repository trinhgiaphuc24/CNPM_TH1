n = int(input("Nhap n: "))
print("-"*10)
print(("*"*n+ "\n") *n)
print("-"*10)
for i in range(n+1):
    print("*"*i + "\n")
print("-"*10)
for i in range(n+1):
    print((" "*(n-i)+"*"*i) + "\n")
print("-"*10)
for i in range(1, n + 1, 2):
    print(("*"*i).center(n) + "\n")