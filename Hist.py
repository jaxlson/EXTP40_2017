'''
Created on 28 nov. 2017

@author: Josefine
'''
import matplotlib
import numpy as np
import pylab as plt
import matplotlib.patches as patches
import matplotlib.path as path

class Hist(object):
    
    def __init__(self, img):
        fig, ax = plt.subplots()
        
        n, bins = np.histogram(img)
        
        # Get the corners of the rectangles for the histogram
        left = np.array(bins[:-1])
        right = np.array(bins[1:])
        bottom = np.zeros(len(left))
        top = bottom + n
        
        
        # we need a (numrects x numsides x 2) numpy array for the path helper
        # function to build a compound path
        XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
        
        # get the Path object
        barpath = path.Path.make_compound_path_from_polys(XY)
        
        # make a patch out of it
        patch = patches.PathPatch(barpath)
        ax.add_patch(patch)
        
        # update the view limits
        ax.set_xlim(left[0], right[-1])
        ax.set_ylim(bottom.min(), top.max())
        
    # return the figure
    def figure(self):
        return plt.gcf()
        