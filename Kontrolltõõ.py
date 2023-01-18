
def print_bunny(n):
    bunny = " (\_/)\n (o.o)\n / | \*"
    for i in range(n):
        print(bunny)
        if i < n-1:
            print("")

num = int(input("sisestage arv vahemikus 1 kuni 9:"))
print_bunny(num)
print()
l = 14
sum = 0

for i in range(l+1):
    sum += i

print(sum)
print()

num = int(input("Sisestage number: "))
sum = 0
product = 1

while num > 0:
    digit = num % 10
    sum += digit
    product *= digit
    num = num // 10

print("Numbrite summa:", sum)
print("Numbrite korrutis:", product)
