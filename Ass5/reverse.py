reverse = ""
a = input("Enter String: ")
for i in range(len(a), 0, -1):
    reverse += a[i-1]
print (reverse)
