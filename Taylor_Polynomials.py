# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:31:14 2020

@author: holme
"""
import numpy as np
import pylab as py
import matplotlib as plt

'''
This program evaluates a 4th degree Taylor polynomials and its errors for 
each value of x in the interval of [-b,b]. The particular function being 
approximates is exp(x) on the interval [-b,b].
'''

# Initialize

n = 4.0
b = 10
h = b/100

#create array for x

def array(b,h):
    x = [-b]
    i = -b
    while i < b:
        i = i + h
        x.append(i)
    return(x)

x = array(b,h)

# factorial function

def fact(n):
    if n == 0:
        return 1
    i = 1
    k = 1
    while i != n+1:
        k = i*k
        i += 1
    return(k)


# numerical exponential function

        
def P1(x,n):
    i = 0
    s = 0
    S = []
    for j in x:
        while i < n:
            s = s + (j**i)/fact(i)
            i += 1
        S.append(s)
        s = 0
        i = 0
    return (S)  

# calculate error

y1 = P1(x,n)
y2 = np.exp(x)

def error(y1,y2):
    err = abs(y1-y2)/y2
    return(err)

# tabular form
title_list  = ["Input Value", "Taylor Ploynomial", "Exponential Function", "Error"]

def PrettyTable(x,y1,y2):
    i = 0
    e = error(y1,y2)
    print('-----------------------------------------------------------------------')
    print ("| Input Value | Taylor Ploynomial  | Exponential Function | Error     |")
    print('-----------------------------------------------------------------------')
    while i < 9:
        print('|   {0:1.2e} |     {1:1.2e}      |      {2:1.2e}        |  {3:1.2e} |'.format(x[i],y1[i],y2[i],e[i]))
        i += 1
    print('|   {0:1.2e} |      {1:1.2e}      |      {2:1.2e}        |  {3:1.2e} |'.format(x[i],y1[i],y2[i],e[i]))
    i += 1
    while i < len(x):
        print('|    {0:1.2e} |      {1:1.2e}      |      {2:1.2e}        |  {3:1.2e} |'.format(x[i],y1[i],y2[i],e[i]))
        i += 1
    print('-----------------------------------------------------------------------')
        
PrettyTable(x,y1,y2)

# plot a pretty plot

plt.plot(x,y1,'b-',x,y2,'r-')
plt.show()

plt.title('Taylor Polynomial for e^x (a = 0)')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend(['Taylor Polynomial', 'Exponential Funciton'])

'''
approximate the function e^2x
'''
# numerical exponential function
        
def P2(x,n):
    i = 0
    s = 0
    S = []
    for j in x:
        while i < n:
            s = s + ((j*2)**(i))/fact(i)
            i += 1
        S.append(s)
        s = 0
        i = 0
    return (S)  

# define new x for true function

def array2(x):
    l = []
    for i in x:
        k = 2*i
        l.append(k)
    return(l)

x2 = array2(x)    

# calculate error

y3 = P2(x,n)
y4 = np.exp(x2)


#plot a pretty plot

plt.plot(x,y3,'b-', x,y4,'r-')
plt.show()

plt.title('Taylor Polynomial for e^2x (a = 0)')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend(['Taylor Polynomial', 'Exponential Funciton'])
    

'''
approximate the function 1-e^x
'''
# numerical exponential function
        
def P3(x,n):
    i = 0
    s = 0
    S = []
    for j in x:
        while i < n:
            s = s + ((j)**(i))/fact(i)
            i += 1
        S.append(1-s)
        s = 0
        i = 0
    return (S)  


# calculate error

y5 = P3(x,n)
y6 = 1-np.exp(x)


#plot a pretty plot

plt.plot(x,y5,'b-', x,y6,'r-')
plt.show()

plt.title('Taylor Polynomial for 1-e^x (a = 0)')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend(['Taylor Polynomial', 'Exponential Funciton'])

'''
Approximating e^x on the interval [-b,b] with less than 0.005 error. 

'''

# a = [1,2,3,4,5,6,7,8,9,10]

# def P(x):
#     S = []
#     i = 0
#     j = 0
#     s = 0
#     n = 1
#     E = 1
#     R = 1
#     for x in a:
#         while 10 > E > 0.05:
#             while i < n:
#                 while j < n+1
#                     s = s + (x**i)/fact(i)
#                     print('s=',s,'i=',i)
#                     R = R + (x**i)/fact(i)
#                     j += 1
#                 i += 1
#             print('s=',s,'R=',R,'E=',E,'n=',n,'x=',x)
#             E = abs(s-R)
#             n += 1
#             i = 0
#             j = 1
#         S.append(s)
#         i = 0
#         j = 1
#         s = 0
#         n = 1
#         E = 1
#     return(S)
                

# y1 = P(x)
# y2 = np.exp(x)

# # plot a pretty plot

# py.figure()
# py.plot(x,y1,'b-',x,y2,'r--')

# py.title('Taylor Polynomial for e^x (a = 0)')
# py.xlabel('X')
# py.ylabel('Y')
# py.xlim(-10,10)
# py.ylim(-10,10)
# py.legend(['Taylor Polynomial', 'Exponential Funciton'])