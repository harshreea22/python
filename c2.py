a=int(input("enter 1st no.:"))
b=int(input("enter 2nd no.:"))
print(a,"is greatest")if(a>b) else print(b,"is greatest")

a=int(input("enter 1st no.:"))
b=int(input("enter 2nd no.:"))
c=int(input("enter 3rd no.:"))
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
smallest=a
if smallest>c:
    smallest=c
if smallest>b:
    smallest=b
if largest==smallest:
    print("all value are same")
else:
    print(largest,"largest",smallest,"smallest")


a=int(input("enter a number:"))
print("even")if(a%2==0) else print("odd")

a=int(input("enter a number:"))
print("divisble by 10")if(a%10==0) else print("non divisble by 10")

age=int(input("enter your age:"))
print("you are able for vote")if(age>=18) else print("you are not able for vote")

a=int(input("enter any digit:"))
n=len(str(a))
print("length is",n)

y=int(input("enter year:"))
print("leap year")if(y%4==0) else print("non leap year")

a=int(input("enter 1st angle:"))
b=int(input("enter 2nd angle:"))
c=int(input("enter 3rd angle:"))
print("valid triangle")if(a+b+c==180) else print("not valid triangle")

a=int(input("enter any value:"))
print("a")if(a>0) else print(a*(-1))

a=int(input("enter length:"))
b=int(input("enter width:"))
area=a*b
perimeter=2*(a+b)
print("true")if(area>perimeter) else print("false")

x1=int(input("x1="))
x2=int(input("x2="))
x3=int(input("x3="))
y1=int(input("y1="))
y2=int(input("y2="))
y3=int(input("y3="))
print("are straight")if((y1-y2)/(x1-x2)==(y1-y3)/(x1-x3)==(y2-y3)/(x2-x3)) else print("are not straight")

x1=int(input("x1="))
y1=int(input("y1="))
r=int(input("radius="))
x=int(input("x="))
y=int(input("y="))
if(((x-x1)^2)+((y-y1)^2)==r^2):
    print("on the circle")
elif(((x-x1)^2)+((y-y1)^2)>r^2):
    print("outside")
else:
    print("inside")

x=int(input("enter a number between 0 to 19:"))
if(x==0):
    print("zero")
elif(x==1):
    print("")
elif(x==2):
    print("two")
elif(x==3):
    print("three")
elif(x==4):
    print("four")
elif(x==5):
    print("five")
elif(x==6):
    print("six")
elif(x==7):
    print("seven")
elif(x==8):
    print("eight")
elif(x==9):
    print("nine")
elif(x==10):
    print("ten")
elif(x==11):
    print("eleven")
elif(x==12):
    print("twelve")
elif(x==13):
    print("thirteen")
elif(x==14):
    print("fourteen")
elif(x==15):
    print("fifteen")
elif(x==16):
    print("sixteen")
elif(x==17):
    print("seventeen")
elif(x==18):
    print("eighteen")
elif(x==19):
    print("nineteen")

sub1=int(input("enter your marks of 1st subject:"))
sub2=int(input("enter your marks of 2nd subject:"))
sub3=int(input("enter your marks of 3rd subject:"))
total=a+b+c
print("total=",total)
avg=total/3
print("average=",avg)
result=avg
print("Grade of subject 1:",end=" ")
if (0<=sub1<=39):
    print("F")
elif (40<=sub1<=44):
    print("P")
elif (40<=sub1<=44):
    print("P")
elif (45<=sub1<=49):
    print("C")
elif (50<=sub1<=54):
    print("B")
elif (55<=sub1<=59):
    print("B+")
elif (60<=sub1<=69):
    print("A")
elif (70<=sub1<=79):
    print("A+")
elif (80<=sub1<=100):
    print("O")
else:
    print("NA")
print("Grade of subject 2:",end=" ")
if (0<=sub2<=39):
    print("F")
elif (40<=sub2<=44):
    print("P")
elif (40<=sub2<=44):
    print("P")
elif (45<=sub2<=49):
    print("C")
elif (50<=sub2<=54):
    print("B")
elif (55<=sub2<=59):
    print("B+")
elif (60<=sub2<=69):
    print("A")
elif (70<=sub2<=79):
    print("A+")
elif (80<=sub2<=100):
    print("O")
else:
    print("NA")
print("Grade of subject 3:",end=" ")
if (0<=sub3<=39):
    print("F")
elif (40<=sub3<=44):
    print("P")
elif (40<=sub3<=44):
    print("P")
elif (45<=sub3<=49):
    print("C")
elif (50<=sub3<=54):
    print("B")
elif (55<=sub3<=59):
    print("B+")
elif (60<=sub3<=69):
    print("A")
elif (70<=sub3<=79):
    print("A+")
elif (80<=sub3<=100):
    print("O")
else:
    print("NA")
print("Final Grade:",end=" ")
if (0<=avg<=39):
    print("F")
elif (40<=avg<=44):
    print("P")
elif (40<=avg<=44):
    print("P")
elif (45<=avg<=49):
    print("C")
elif (50<=avg<=54):
    print("B")
elif (55<=avg<=59):
    print("B+")
elif (60<=avg<=69):
    print("A")
elif (70<=avg<=79):
    print("A+")
elif (80<=avg<=100):
    print("O")
else:
    print("NA")