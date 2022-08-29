#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 08:16:12 2021 

@author: Eshagh Dehmollaian
"""
# Import required libraries
import numpy as np
################
def bin2matnp(Input,receiver_num):
    if receiver_num==1:
        input_numpy = np.fromfile(str(Input), dtype=np.float32)
        input_numpy_ = array_to_matrix(input_numpy)
        input_numpy_ = input_numpy_-29*np.ones(np.shape(input_numpy_))#power reference of R1 is 29dB
    elif receiver_num==2:
        input_numpy = np.fromfile(str(Input), dtype=np.float32)
        input_numpy_ = array_to_matrix(input_numpy)
        input_numpy_ = input_numpy_-14*np.ones(np.shape(input_numpy_))#power reference of R2 is 14dB
    else:
        raise ValueError("Wrong number was assigned in the second argument!!")
    return input_numpy_    
################
def array_to_matrix(array_input):
    if len(array_input)%208!=0:#number of subcarrier is 208
        raise ValueError("BOOM")
    return np.reshape(array_input,(int(len(array_input)/208),208))    
################  
# Import any dataset file you want from Hall or Office directory, I chose office_r1A_R1
O_r1A_R1 = bin2matnp('office_r1A_R1.float',1)
# Now, "O_r1A_R1" is a NumPy array that you can proceed with that...

