"""
==========================================================
Programmer: Benjamin Malz, with a little help from John D. Cook.
Summary:     This program takes input from users to find the distance between
two locations in miles and kilometers and determines what travel method to use 
to traverse between the two locations.

INPUT:  Users input the name of two locations as well as the coordinates of two
locations.
        
OUTPUT: The distances between two locations in meters and kilometers, and 
suggested travel method.
Example below:
-------------------------------
-DISTANCES BETWEEN COORDINATES-
-------------------------------
Sample coordinates:  41.9667526,  -71.1870159  
	(Notice a COMMA is needed between the pair)


Enter name of the place: Randomtown
Enter latitude, longitude coordinates: 41.88, -22.12
-----------------------------------
Sample coordinates:  41.9667526,  -71.1870159  
	(Notice a COMMA is needed between the pair)


Enter name of the place: Othertown
Enter latitude, longitude coordinates: 43.88, -22.52
-----------------------------------
--------------------------------------------------
Randomtown:
 [41.880000, -22.120000]
    \
     \
      ------ 
            \
             \
	Othertown:
	 [43.880000, -22.520000]
--------------------------------------------------
Distance between locations in miles:  139.7061525801153
Distance between locations in Kilometers:  223.52984412818446
You should drive.

Done.

Date Last Modified:
 09/10/2016:  (mdl) Starter Kit created
 09/19/2016: Completed the program. Learned never to procrastinate again.
 Bug tested for hours, finally fixed error. Added comments and information.
========================================================== 
"""


import math
# ======================================================
def convertMilesToKM( miles ):
    
    convertMilesToKM = (miles * 1.6)
   
    return convertMilesToKM
  
# ======== end convertMilesToKM() ======================
    
# ======================================================
def convertKmToMiles( km ):

    convertKmToMiles = (km * 1.609344)
    
    return convertKmToMiles

# ======== end convertKmToMiles() ======================


# ======================================================
def distanceBetweenPoints( lat1, long1, lat2, long2 ):
    
    import math
     
     
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
     
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
     
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians 
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
    math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return arc
    
 #Thanks, John D. Cook!
# ======== end distanceBetweenPoints() =================
  

# ======================================================
def enterPlace():
    
    print ("Sample coordinates:  41.9667526,  -71.1870159  ")
    print ("\t(Notice a COMMA is needed between the pair)\n\n")
    
    where = input("Enter name of the place: ")
    latitude, longitude = eval(input("Enter latitude, longitude coordinates: "))
    print ("-----------------------------------")
    
    return where, latitude, longitude

# ======== end enterPlace() ===================

# ======================================================
def echoTwoCoordinates(where1, lat1, long1, where2, lat2, long2):
    
    print ("--------------------------------------------------")
    print ("%s:\n [%.6f, %.6f]" % (where1, lat1, long1) )
    print ("    \\")
    print ("     \\")
    print ("      ------ ")
    print ("            \\")
    print ("             \\")
    print ("\t%s:\n\t [%.6f, %.6f]" % (where2, lat2, long2) )
    print ("--------------------------------------------------")
    
    
# ======== end echoTwoCoordinates() ====================

def printTitle():
    print("-------------------------------")
    print("-DISTANCES BETWEEN COORDINATES-")
    print("-------------------------------")

# ======================================================
def main():

    
    print("\n\n")
    
    # (0) print title (call your function)
    printTitle()


    
    # (1) get the input pairs (call your function)
    where1, lat1, long1 = enterPlace()
    where2, lat2, long2 = enterPlace()
    #these variables hold the name, latitude and longitude entered by a user.
    
    # or "fake input" during testing by setting sample points
    """
    where1 = "somewhere"
    lat1 =  1.23
    long1 = 4.56
    where2 = "elsewhere"
    lat2 = 54.23
    long2 = -12.21
    """
    
    """ Sample inputs
    "Wheaton College, Norton, MA, USA"
     41.9667526  
    -71.1870159

    "near campus, Norton, MA, USA"
     41.962696  
    -71.189858
    
    "Attleboro, MA, USA"
     41.944487  
    -71.284098
 
    "Jay, ME, USA"
     44.479866  
    -70.196829  
    
    "Shanghai, China"
     31.230393  
    121.473704
    """


    # (2) echo (print on the console) the inputs
    echoTwoCoordinates(where1, lat1, long1, where2, lat2, long2)
    
    
    # (3) now call distanceBetweenPoints to compute the distance
    distanceBetweenPoints(lat1, long1, lat2, long2)
    
    
    
    
    # (4) then convert to distance on the radius of the earth (in miles)
    miles = distanceBetweenPoints(lat1,long1,lat2,long2) * RADIUS_EARTH_MILES 
    #stores the converted distance in miles.
    km = convertMilesToKM(miles)
    #stores miles converted into kilometers.
    
    
    
    
    print ("Distance between locations in miles: ", miles)
    print ("Distance between locations in Kilometers: ", km)
    
    
    
    
    # (5) now print an appropriate message on how to travel using if-elif-else
    if (miles <= 1):
        print("You should walk.")
    elif (miles <= 500):
        print("You should drive.")
    else:
        print("You should fly.")
    


 
    print ("\nDone.")
    
# ======== end main() =================================
    
    

# program STARTS HERE ...
#-----------------------------------------------------
if __name__ == '__main__':
    
    # declare some global variables
    RADIUS_EARTH_MILES = 3960

    # declare other global variables you need below
    RADIUS_EARTH_KM = 6371
    
    
    
    main()
#-----------------------------------------------------
    
    
