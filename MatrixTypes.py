import numpy as np


class Matrix(object):
    def __init__(self,arr):
        self.arr = arr

    def Matrix4x4(self):
        upper_half = np.hsplit(np.vsplit(self.arr, 2)[0], 2)
        lower_half = np.hsplit(np.vsplit(self.arr, 2)[1], 2)
        upper_left = upper_half[0]
        for i in range (len(upper_left)):upper_left[i] = 1
        upper_right = upper_half[1]
        for i in range (len(upper_right)):upper_right[i] = 2   
        lower_left = lower_half[0]
        for i in range (len(lower_left)):lower_left[i] = 3
        lower_right = lower_half[1]
        for i in range (len(lower_right)):lower_right[i] = 4

       
        x=np.vstack([np.hstack([upper_left, upper_right]), np.hstack([lower_left, lower_right])])
        return x



    def Matrix9x9(self):
        upper_half = np.hsplit(np.vsplit(self.arr, 3)[0], 3)
        mid_part = np.hsplit(np.vsplit(self.arr, 3)[1], 3)
        lower_half = np.hsplit(np.vsplit(self.arr, 3)[2], 3)

        upper_left = upper_half[0]
        for i in range (len(upper_left)):upper_left[i] = 1        
        upper_mid = upper_half[1]
        for i in range (len(upper_mid)):upper_mid[i] = 2
        upper_right = upper_half[2]
        for i in range (len(upper_right)):upper_right[i] = 3


        mid_left = mid_part[0]
        for i in range (len(mid_left)):mid_left[i] = 4
        center = mid_part[1]
        for i in range (len(center)):center[i] = 5
        mid_right = mid_part[2]
        for i in range (len(mid_right)):mid_right[i] = 6


        lower_left = lower_half[0]
        for i in range (len(lower_left)):lower_left[i] = 7
        lower_mid = lower_half[1]
        for i in range (len(lower_mid)):lower_mid[i] = 8
        lower_right = lower_half[2]    
        for i in range (len(lower_right)):lower_right[i] = 9

        x=np.vstack([np.hstack([upper_left, upper_mid, upper_right]),np.hstack([mid_left,center, mid_right]), np.hstack([lower_left,lower_mid, lower_right])])
        return x

    def Matrix16x16(self):
        upper = np.hsplit(np.vsplit(self.arr, 4)[0], 4)
        mid_top = np.hsplit(np.vsplit(self.arr, 4)[1], 4)
        mid_lower = np.hsplit(np.vsplit(self.arr, 4)[2], 4)
        lower = np.hsplit(np.vsplit(self.arr, 4)[3], 4)

        upper_left = upper[0]
        for i in range (len(upper_left)):upper_left[i] = 1  
        upper_left_mid = upper[1]
        for i in range (len(upper_left_mid)):upper_left_mid[i] = 2  
        upper_right_mid = upper[2]
        for i in range (len(upper_right_mid)):upper_right_mid[i] = 3  
        upper_right = upper[3]
        for i in range (len(upper_right)):upper_right[i] = 4  

        mid_top_left = mid_top[0]
        for i in range (len(mid_top_left)):mid_top_left[i] = 5  
        mid_top_left_mid = mid_top[1]
        for i in range (len(mid_top_left_mid)):mid_top_left_mid[i] = 6  
        mid_top_right_mid = mid_top[2]
        for i in range (len(mid_top_right_mid)):mid_top_right_mid[i] = 7  
        mid_top_right = mid_top[3]
        for i in range (len(mid_top_right)):mid_top_right[i] = 8

        mid_lower_left = mid_lower[0]
        for i in range (len(mid_lower_left)):mid_lower_left[i] = 9  
        mid_lower_left_mid = mid_lower[1]
        for i in range (len(mid_lower_left_mid)):mid_lower_left_mid[i] = 10  
        mid_lower_right_mid = mid_lower[2]
        for i in range (len(mid_lower_right_mid)):mid_lower_right_mid[i] = 11  
        mid_lower_right = mid_lower[3]
        for i in range (len(mid_lower_right)):mid_lower_right[i] = 12  

        lower_left =  lower[0]
        for i in range (len(lower_left)):lower_left[i] = 13  
        lower_left_mid = lower[1]
        for i in range (len(lower_left_mid)):lower_left_mid[i] = 14  
        lower_right_mid =lower[2]
        for i in range (len(lower_right_mid)):lower_right_mid[i] = 15  
        lower_right = lower[3]
        for i in range (len(lower_right)):lower_right[i] = 16  



        x=np.vstack([
        np.hstack([upper_left,upper_left_mid,upper_right_mid,upper_right]),
        np.hstack([mid_top_left,mid_top_left_mid,mid_top_right_mid,mid_top_right_mid]), 
        np.hstack([ mid_lower_left,mid_lower_left_mid,mid_lower_right_mid,mid_lower_right]),
        np.hstack([ lower_left,lower_left_mid,lower_right_mid,lower_right])])
        return x