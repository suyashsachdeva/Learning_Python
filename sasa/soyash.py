#number of ways in which n number of people will go to a parwy with 2 being the maximum number of people gong together
def prob(n):
    if n==1:
        return 1
    if n==2:
        return 2    
        
    else:
        m=n-1
        return prob(n-1)+(m*prob(n-2))
print("hello")
i=int(input("no. of people going in the parwy "))
u=prob(i)

print("The number of ways in which people"+str(i)+ "can come to "+str(u))


                


                