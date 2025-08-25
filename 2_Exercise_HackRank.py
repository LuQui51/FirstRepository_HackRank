#A simple code to print a pattern based on user input

N, M = map(int,input().split())

for i in range(int((N-1)/2)):
    print((".|."*(1+i*2)).center(M,"-"))

print("WELCOME".center(M,"-"))

for j in range(int((N-1)/2)-1, -1, -1):
    print((".|."*(1+j*2)).center(M,"-"))