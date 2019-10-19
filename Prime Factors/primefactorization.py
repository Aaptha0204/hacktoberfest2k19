n=int(input("Enter an integer:"))
i=1; c=0
while i<n:
    j=1;f=0
    if(n%i==0):
           while j<i:
                   if(i%j==0):
                        f=f+1
                       j=j+1
     if(f==1):
        c=c+1
 print('the number of prime factors are',c)
