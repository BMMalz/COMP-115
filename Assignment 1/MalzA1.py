"""
==========================================================
Programmer:  Benjamin Malz
Summary:    This program computes the distances and slopes between points
as well as the average and total of the distances.

INPUT (keyboard, stdin):  User must input their coordinates into their
respective variables, beginning on line 56. This is not true input, but is
for faster testing.
        
        
      Potential Error: When first x value is the same as second x value you will
      get an error. You cannot divide by zero.
        
        
OUTPUT (console, stdout): The points of gaze fixation, the distances and slopes
between the points, and the average and total of the distances between points.


Date Last Modified:
 08/22/2016:  (mdl) Starter Kit created
 08/23/2016:  (mdl) more details added 
 09/08/2016: added other x coordinates, added formulas, got float error.
 09/09/2016: debugging, solve float error, finish program, remove clutter in
 code, fixed MAJOR indent inconsistency. 
========================================================== 
"""

import math


# ======================================================
def distance(x1,y1,x2,y2):
    
   dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
   return dist
# ======== end distance() ==============================


# ======================================================
def slope( x1, y1, x2, y2 ):
    
   slope = (y2 - y1)/(x2 - x1)
    
   return slope
# ======== end slope() =================================



# ======================================================
def main():
    
   print ("\n\n")
  
   
   x1 = 90.0     
   y1 = 10.0
   x2 = 05.0
   y2 = 40.0
   x3 = 10.0
   y3 = 30.0
   x4 = 50.0
   y4 = 25.0
    
   print ("|--------------------------------------------|")
   print ("| Data for four gaze points in (x,y) format. |")
   print ("| All numbers are in units of pixels.        |")
   print ("|--------------------------------------------|")
   print ("")
    
   # ECHO (x,y) coordinates to the console (stdout) here
   print ("Gaze Fixation (1): (%5.1f,%5.1f)"   % (x1,y1) )
   print ("Gaze Fixation (2): (%5.1f,%5.1f)"   % (x2,y2) )
   print ("Gaze Fixation (3): (%5.1f,%5.1f)"   % (x3,y3) )
   print ("Gaze Fixation (4): (%5.1f,%5.1f)"   % (x4,y4) )
   dist1_2 = distance(x1,y1,x2,y2)  
   dist2_3 = distance(x2,y2,x3,y3)
   dist3_4 = distance(x3,y3,x4,y4)
   slope1_2 = slope(x1,y1,x2,y2)
   slope2_3 = slope(x2,y2,x3,y3)
   slope3_4 = slope(x3,y3,x4,y4)
   print ("Distance from point 1 to point 2 is: %5.2f" % dist1_2)
   print ("Slope between point 1 and point 2 is: %5.2f" % slope1_2)
   print ("Distance from point 2 to point 3 is: %5.2f" % dist2_3)
   print ("Slope between point 2 and point 3 is: %5.2f" % slope2_3)
   print ("Distance from point 3 to point 4 is: %5.2f" % dist3_4)
   
   
   print ("Slope between point 3 and point 4 is: %5.2f" % slope3_4)
   totald = dist1_2 + dist2_3 + dist3_4
   avgd = totald/3
   print ("The total distance between the points is: %5.2f" % totald)
   print ("The average distance between the points is: %5.2e" % avgd)
    
   print ("\nEnd program.")
    
# ======== end main() =================================
   
    

# program STARTS HERE ... 
# (don't change this; this makes Python run main first)
#-----------------------------------------------------
if __name__ == '__main__':
    main()
#-----------------------------------------------------    