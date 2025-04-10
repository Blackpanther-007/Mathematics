import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animtn
import pandas as pd

# def Func(x1,x2):


# def min_err(Augmented, N, C, D):#augmented matrix is matrix with all input and out put with augmented results for particular x1 and N is number of datasets we have
#     A = Augmented
#     err_squre = 0
#     for i in range(N):
#         err_squre += np.square((C*A[i][0]) + (D*A[i][1])-(A[i][2]))
    
    
def Find_value_of_C_D():
    A = np.matrix([np.ones_like(x_1), x_1])

df = pd.read_csv('C:/Users/HP/Documents/codes/Mathematics/least_square/dataset.csv')
print(df.head)
print(df['x1'])

