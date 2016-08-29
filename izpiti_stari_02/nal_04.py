num = int(input("Enter a number"))

base = 2
result = 0.0


for i in range(0, num+1):
    result += pow(base, -i)

print(result)

