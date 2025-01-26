a=44
b=34
print(a+b)
print(a-b)
print(a*b)
print(a/b)

hour=int(input("enter hour:"))
minute=hour*60
print(minute)

minute=int(input("enter minute:"))
hour=minute/60
print(hour)

dollar=int(input("enter dollar:"))
rupees=dollar*48
print(rupees)

rupees=int(input("enter rupees:"))
dollar=rupees/48
print(dollar)

dollar=int(input("enter dollar:"))
pound=70/48*dollar
print(pound)

gram=int(input("enter gram:"))
kg=gram/1000
print(kg)

kg=int(input("enter kg:"))
gram=kg*1000
print(gram)

byte=int(input("enter byte:"))
KB=1000*byte
MB=1000000*byte
GB=1000000000*byte
print(KB,MB,GB)

C=int(input("enter C:"))
F=(9/5*C)+32
print(F)

F=int(input("enter fahrenheit:"))
C=5/9*(F-32)
print(C)

P=int(input("enter amount:"))
R=int(input("enter rate:"))
T=int(input("enter time:"))
I=P*R*T/100
print(I)

l=int(input("enter length:"))
area=l*l
perimeter=4*l
print(area,perimeter)

a=int(input("enter length:"))
b=int(input("enter width:"))
area=a*b
perimeter=2*(a+b)
print(area,perimeter)

r=int(input("enter radius:"))
area=22/7*r*r
print(area)

l=int(input("enter length:"))
h=int(input("enter height:"))
area=1/2*l*h
print(area)

grosssalary=int(input("enter gross salary:"))
allowance=grosssalary*10/100
deduction=grosssalary*3/100
netsalary=grosssalary+allowance-deduction
print(netsalary)

grosssales=int(input("enter gross sales:"))
discount=grosssales*10/100
netsales=grosssales-discount
print(netsales)

a=int(input("enter your maths marks:"))
b=int(input("enter your physics marks:"))
c=int(input("enter your chemistry marks:"))
average=(a+b+c)/3
print(average)

a=int(input("enter any number:"))
b=int(input("enter other number:"))
a=a+b
b=a-b
a=a-b
print(a,b)