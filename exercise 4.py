maths = int(input("maths: "))
eng = int(input("english: "))
phyc = int(input("physics: "))
chem = int(input("chemistry: "))
bio = int(input("biology: "))

sum = maths + eng + phyc + chem + bio

average = sum/5


if average > 70 and average <= 100:
    print("A")

elif average > 60 and average <= 70:
    print("B")

elif average > 50 and average <= 60:
    print("C")

elif average >= 40 and average <= 50:
    print("D")

elif average >= 0 and average <= 39:
    print("E")
else:
    print("invalid number")

#print(average)

