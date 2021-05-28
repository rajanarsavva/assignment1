# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEliIo4NBZZdtLjVXs7ulS7p9vexLlXn
"""



import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

import numpy as np

A = np.array([[0, -2, 1], [1, -np.sqrt(3), 0], [1, 1, 1]])
B = np.array([0, 0, 11])
X2 = np.linalg.inv(A).dot(B)

print(X2)

#Triangle sides
a = X2[0]
b = X2[1]
c = X2[2]

#Coordinates of A
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)

#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0])

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] + 0.1, A[1]  + 0.1 , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] , B[1]  + 0.1 , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]  + 0.1, C[1]  + 0.1 , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#else
#plt.show()