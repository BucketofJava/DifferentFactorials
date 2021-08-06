import math

def nfactorial(num, n):
  if(num<3):
    return num;
  finalnum=num;
  while num>n:
    num-=n;
    finalnum*=num;
  return finalnum;
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
#So that it doesnt get covered up by the little thing in the top right corner of the console output

print("\n")
print(superFactorialPickover(30))
print(nfactorial(45, 3))

