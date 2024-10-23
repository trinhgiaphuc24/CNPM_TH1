import random
#n = int(input("Nhap n: "))
#a = [int(input(f"a[{i}] = ")) for i in range(n)]
a = [random.randint(-10, 10) for i in range(5)]
for i in range(5):
    print(f"a[{i}] = {a[i]}")
print(a)
b = [x for x in a if x > 0]
c = [x for x in a if x < 0]
print("Max:", max(b) if len(b) > 0 else "*")
print("Min:",min(c) if len(c) > 0 else "*")
for x in set(a):
    print(f"{x} xuat hien {a.count(x)} lan")