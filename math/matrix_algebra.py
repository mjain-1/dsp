# Matrix Algebra
import numpy as np

#1. Matrix Dimensions

##1.1
a = np.array([[1,2,3],[2,7,4]])
print (a.shape)
#(2, 3)

##1.2
b = np.array([[1, -1],[0,1]])
print (b.shape)
#(2,2)

##1.3
c = np.array([[5, -1], [9, 1], [6, 0]])
print (c.shape)
#(3,2)

##1.4
d = np.array([[3, -2, -1], [1, 2, 3]])
print (d.shape)
#(2, 3)

##1.5
u = np.array([[6, 2, -3, 5]])
print (u.shape)
#(1, 4)


##1.6
w = np.array([[1],[8],[0],[5]])
print (w.shape)
#(4, 1)


#2. Vector Operations

##2.1
print (u+v)
#[9, 7, -4, 9]

##2.2 
print (u-v)
#[3, -3, -2, 1]

##2.3 
print (6*u)
#[36, 12, -18, 30]

##2.4
print (np.vdot(u, v))
# 51

##2.5
print (np.linalg.norm(u))
# 8.6023252670426267

#3. Matrix Operations

##3.1
print (a + c)
# Not defined

##3.2
print (a - c.T)
#array([[-4, -7, -3], [ 3,  6,  4]])

##3.3
print (c.T + 3*d)
#array([[14,  3,  3], [ 2,  7,  9]])

##3.4
print (np.dot(b, a))
#array([[-1, -5, -1], [ 2,  7,  4]])

##3.5
print (np.dot(b, a.T))
#Not defined

#Optional

##3.6
print (np.dot(b, c))
#Not defined

##3.7
print (np.dot(c,b))
#array([[ 5, -6], [ 9, -8], [ 6, -6]])

##3.8
print (np.linalg.matrix_power(b, 4))
#array([[ 1, -4], [ 0,  1]])

##3.9
print (np.dot(a, a.T))
#array([[14, 28], [28, 69]])

##3.10
print (np.dot(d.T, d))
#array([[10, -4,  0], [-4,  8,  8], [ 0,  8, 10]])
