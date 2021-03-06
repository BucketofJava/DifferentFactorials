import math
import util



#More accurate, but slower for bigger numbers
def nfactorial(num, n):
  if(num<3):
    return num;
  finalnum=num;
  while num>n:
    num-=n;
    finalnum*=num;
  return finalnum;
#Less accurate(Not by that much), but quicker for bigger numbers. Use n=1 for normal factorial.
def nfactorialefficient(num, n=1):
  if(num<3 and n!=1):
    return num;
  tennum=math.trunc(math.log(num, 10))
  finalnum=num/(10**tennum);
  while num>n:
    num-=n;
    finalnum*=num;
    tennumi=math.trunc(math.log(finalnum, 10));
    tennum+=tennumi;
    finalnum/=(10**tennumi);
  string="{} * 10^{}".format(finalnum, tennum)
  return finalnum, tennum, string;
def subfactorial(num):
  finalnum=0;
  for i in range(num-1):
    finalnum+=((-1)**(i+2))*(1/math.factorial(i+2))
  finalnum*=math.factorial(num);
  return finalnum;
def primorial(num):
  finalnum=num;
  for i in util.sieveOfEratosthenes(num):
    finalnum*=i;
  return finalnum;
def superFactorialSloane(num):
  tennum=0;
  finalnum=1;
  for i in range(num):
    finalnum*=math.factorial(num-i)
    tennumi=math.trunc(math.log(finalnum, 10));
    tennum+=tennumi;
    finalnum/=(10**tennumi);
  string="{} * 10^{}".format(finalnum, tennum)
  return finalnum, tennum, string;  
def superFactorialPickover(num):
  tennum=math.trunc(math.log(num, 10))
  finalnum=num/(10**tennum);
  for i in range(num-1):
    tennum*=num;
    finalnum=finalnum**num;
    tennumi=math.trunc(math.log(finalnum, 10));
    tennum+=tennumi;
    finalnum/=(10**tennumi);
  string="{} * 10^{}".format(finalnum, tennum)
  return finalnum, tennum, string;
def exponentialFactorial(num):
  tennum=0;
  finalnum=num;
  for i in range(num-1):
    finalnum=finalnum**(num-(i+1))
    tennum*=(num-(i+1));
    tennumi=math.trunc(math.log(finalnum, 10));
    tennum+=tennumi;
    finalnum/=(10**tennumi);
  string="{} * 10^{}".format(finalnum, tennum)
  return finalnum, tennum, string;  
def hyperFactorial(num):
  tennum=0;
  finalnum=1;
  for i in range(num):
    finalnum*=math.pow(num-i, num-i)
    tennumi=math.trunc(math.log(finalnum, 10));
    tennum+=tennumi;
    finalnum/=(10**tennumi);
  string="{} * 10^{}".format(finalnum, tennum)
  return finalnum, tennum, string;  
#The new line is so that it doesnt get covered up by the little thing in the top right corner of the console output
print("\n")
print("Leave a blank to skip a function")
nfactorialnum=input("Enter what number you would like to use\n for the n factorial function:  ")
nfactorialnum2=input("Enter what number you would like to use\n as the number of exclamation points for the n factorial function:  ")
if(nfactorialnum!=""):
  print(nfactorialefficient(int(nfactorialnum), int(nfactorialnum2))[2])
subfactorialnum=input("Enter what number you would like to use\n for the subfactorial function:  ")
if(subfactorialnum!=""):
  print(subfactorial(int(subfactorialnum)))
primorialnum=input("Enter what number you would like to use\n for the primorial function:  ")
if(primorialnum!=""):
  print(primorial(int(primorialnum)))
sloanesuperfactorialnum=input("Enter what number you would like to use\n for the sloane superfactorial function:  ")
if(sloanesuperfactorialnum!=""):
  print(superFactorialSloane(int(sloanesuperfactorialnum))[2])
pickoversuperfactorialnum=input("Enter what number you would like to use\n for the pickover superfactorial function:  ")
if(pickoversuperfactorialnum!=""):
  print(superFactorialPickover(int(pickoversuperfactorialnum))[2])
exposuperfactorialnum=input("Enter what number you would like to use\n for the exponential factorial function:  ")
if(exposuperfactorialnum!=""):
  print(exponentialFactorial(int(exposuperfactorialnum))[2])
hypsuperfactorialnum=input("Enter what number you would like to use\n for the hyper factorial function:  ")
if(hypsuperfactorialnum!=""):
  print(hyperFactorial(int(hypsuperfactorialnum))[2])

