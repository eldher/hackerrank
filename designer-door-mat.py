n,m = input().split()

n = int(n)
m = int(m)

for i in range((n-1)//2):
    c = ".|."
    print((c*(i+1+(1*i))).center(m,"-"))

print("WELCOME".center(m,"-"))

for i in reversed(range((n-1)//2)):
    c = ".|."
    print((c*(i+1+(1*i))).center(m,"-"))
