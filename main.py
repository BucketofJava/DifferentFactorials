import math

# Code from: <dickinsm@gmail.com>, Nov 30 2006
#http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

def nfactorial(num, n):
  if(num<3):
    return num;
  finalnum=num;
  while num>n:
    num-=n;
    finalnum*=num;
  return finalnum;
def primorial(num):
  finalnum=num;
  for i in sieveOfEratosthenes(num):
    finalnum*=i;
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
print(primorial(7))

