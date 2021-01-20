# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:56:39 2021

@author: holme
"""
import numpy as np
import matplotlib.pylab as plt

# function cos(x); intg(0->pi/2) cos(x) dx = 1
def f(x):
    return(np.cos(x))
a = 0
b = np.pi/2
N = 10
t = 1.00

def error(t,e):
    return(abs(t-e)/t)

# Reinman Sum's
def Reinman(a,b,N):
    h = (b-a)/float(N)
    x = np.linspace(a,b,N+1)
    y = f(x)
    R = np.sum( h*y[1::1])
    return(R)

R = Reinman(a,b,N)
err = error(t,R)
print('Reinman = ',R , ', err = ', err, ', N = ', N)


# Trapezoidal Rule

def Trapezoid(a,b,N):
    h = (b-a)/float(N)
    x = np.linspace(a,b,N+1)
    y = f(x)
    T = (h)*(0.5*y[0] + np.sum( y[1:-2:1]) + 0.5*y[-1])
    return(T)

T = Trapezoid(a,b,N)
err = error(t,T)
print('Trapezoid = ',T, ', err = ', err, ', N = ', N)

# Simpson's Rule

def Simpsons(a,b,N):
    if N %2 ==1:
        raise ValueError("N must be an even integer.")
    h = (b-a)/float(N)
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = (h/3)*np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return(S)

S = Simpsons(a,b,N)
err = error(t,S)
print('Simpson = ',S, ', err = ', err, ', N = ', N)
    
# Gaussian quadrature

# def Gaussian(a,b,N):
#     return()

# G = Gaussian(a,b,N)
# err = error(t,G)
# print('Gaussian = ', G, ', err = ', err, ', N = ', N)

# Multiple Dimensions

a = 0
b = np.pi/2
c = 0
d = np.pi/2
N = 10
t = 1.00

def Surface(a,b,c,d,N):
    hx = (b-a)/float(N)
    hy = (d-c)/float(N)
    s = 0
    i = 0
    j = 0
    while i < N + 1:
        while j < N + 1:
            x = a + hx/2 + i*hx
            y = c + hy/2 + j*hy
            s = s + (hx*hy)*np.sin(x,y)
            j += 1
        i += 1
    return(s)


TwoD = Surface(a,b,c,d,N)
err = error(t,TwoD)
print('Surface = ',TwoD , ', err = ', err, ', N = ', N)

