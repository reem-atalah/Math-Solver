
import numpy as np
from math import log10,sin,pi,log,cos,tan,sqrt


#A function which calculates Trapezoidal
def TrapezoidalIntegration(g,a,b,n): #g is queation,a is lower bound, b is upper bound,n is number of segment
    h=(b-a)/float(n)
    h=float(h)
    answer=0.0
    for iterator in np.arange(a,b,h):
        if iterator==a :
            answer+=g(iterator)
   
        else:   
            answer+=2*g(iterator)
    answer+=g(b)
    answer*=h/2
    #print(answer)
    return answer

theFuntion=input("enter quation :")
g= lambda x:eval(theFuntion)
a=input("please enter the lower bound:")
a=float(a)
b=input("please enter the upper bound:")
b=float(b)
n=input("please enter n:")
n=float(n)

temp=TrapezoidalIntegration(g,a,b,n) # t4aboh el variables da m3 el parameters bta3t el function sodfa m4 aktr XD 
print(temp)
#######################################################################################


#     x*sqrt((16-x**2)**3)












