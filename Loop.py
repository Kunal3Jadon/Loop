#1..WAP to check if the number is an Armstrong number or not
num=int(input())
sum=0
temp=num
while temp > 0:
   d=temp%10
   sum+=d**3
   temp//=10
if num==sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#2..WAP to check no is perfect number or not
n=int(input())
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1=sum1+i
if (sum1==n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
#3..WAP to print table of a number
n=int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
#4..WAP to chech no is neon number or not
num=int(input())
sqr=num*num
sum=0
while sqr>0:
    sum=sum+sqr%10
    sqr=sqr//10

if (num==sum):
    print("Neon Number")
else:
    print("Not a Neon Number")
#4..WAP to Check the Number is a Krishnamurthy Number/strong/peterson
a=int(input())
g=a
fact=1
sum=0
while(a>0):
     r=a%10
     fact=1
     for i in range(1,r+1):
         fact=fact*i
     sum=sum+fact
     a=a//10
if(sum==g):
 print("Krishnamurthy Number")
else:
    print('not')
#5..WAP to print armstrong numbers between 1 and 1000
for num in range(1,1001):
   order=len(str(num))
   sum=0
   temp=num
   while temp > 0:
       digit=temp%10
       sum+=digit**order
       temp//=10

   if num==sum:
       print(num)


































        
