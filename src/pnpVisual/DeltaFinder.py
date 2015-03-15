'''
Created on 15.03.2015

@author: Bastian
'''
import cv2
import numpy as np


class DeltaFinder(object):
    '''
    Finds the delta to a given image in x,y and rotation
    '''
    borderColor = (255,0,0) # blue
    

    def __init__(self, act_img, ref_img):
        '''
        load both images bv
        '''
        
        self.actual = cv2.imread(act_img)#, cv2.IMREAD_GRAYSCALE)
        im_x,im_y = self.actual.shape[1],self.actual.shape[0] #new size (w,h)
        self.reference = cv2.resize(cv2.imread(ref_img), (im_x,im_y))
        imgray = cv2.cvtColor(self.actual,cv2.COLOR_BGR2GRAY)

        ret, act_thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(act_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
        
            #for the first countour
            #cnt = contours[4]
            #cv2.drawContours(self.actual, [cnt],0, (0,255,0), 1)
            
            area = cv2.contourArea(cnt)
            perimeter = cv2.arcLength(cnt, True)
            epsilon = 0.1*cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
#            cv2.polylines(self.actual, [approx], True, (0,0,255),1)
            
            rect = cv2.minAreaRect(cnt)
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(self.actual, [box],0,(127,0,127),2)
        
        
        #cv2.drawContours(self.actual, approx,0, (0,255,0), 1)
        
        #cv2.line(self.actual, (0,0),(100,100),(255,0,0),5)
        
#        cv2.imshow('current image', self.actual)
        cv2.imshow('referenced image', cv2.addWeighted(self.actual,0.8, self.reference,0.2, 0))
        cv2.waitKey(0)
        cv2.destroyAllWindows()