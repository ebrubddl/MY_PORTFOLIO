beginning=int(input("What is the first number?: "))
ending=int(input("What is the last number?: "))
rangee=int(input("How many it will increase?: "))

Number=0
for n in range(beginning,ending+1,rangee):
    Number+=n
print(Number)
