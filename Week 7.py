print("Hello, World!")
x=3
hello="banna"
apple="3.14159265358"
print(apple)
george="It was a bright cold day in April, and the"
print(george)
from sympy.abc import x
from sympy import *
print(sin(3*x))
from sympy.abc import theta

f=cos(3*theta)

print(f.subs(theta,1.5))

from sympy import *
x1 = symbols("x1")
x2 = symbols("x2")

print(solve([2*x1 + 5*x2 - 9,3*x1 - 2*x2 -41]))

A=2
B=3
if A == 1:
    print("A is equal to 1")
print("This code runs whatever the value of A")    

if not A==1:
    print ("A is not equal to 1")

if A==1 and B==7:
    print ("A is equal to 1 and B is equal to 7")

if A==1 or B==3:
    print ("A is equal to 1, B is equal to 3 or both")

if A == 1:
    print("A is equal to one")

elif A == 7:
    print ("A is equal to seven")

else:
    print ("A is not equal to either one or seven")

from sympy import *
from sympy.abc import x
f = 3*x**4+7*x**2+6

if f.subs(x,-x) == f:
    print("even")
elif f.subs(x,-x) == -f:
    print("not even")
else:
    print("neither")    





















    
