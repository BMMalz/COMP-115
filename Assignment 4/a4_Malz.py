"""
==========================================================
Programmer:  Benjamin Malz
Summary:     This program reads DNA from a .fna file, and then determines
whether or not the DNA proves that a person has Huntington's Disease.


INPUT (keyboard, stdin):  The program prompts users through a menu to enter a
number to perform an action. The user must type a filename by pressing '1' first
before they can do anything else.
        
        
INPUT (from a file of data): The .fna file contains a segment of DNA which can
be used to determine if someone has Huntington's Disease.
     
        
OUTPUT (console, stdout): The shell will display a menu which can be 'interacted'
with by pressing 1, 2, 3 and 4. The interactions will yield: a reading of the .fna
file's DNA, the number of CAG repetitions in the DNA, whether or not someone has
Huntington's Disease, and the percentage of the DNA that is the letters 'C' and
'G'. 

Date Last Modified:
 10/10/2016:  (mdl) Starter Kit created
 10/17/2016: (BMM) Finished the getDna() portion of the code.
 10/19/2016: (BMM) CG Percentage added, CAG repeat detection added and classifications
 for Huntington's Disease added.
========================================================== 
"""
import os

# ------ CONSTANTS for entire file ----------

# menu options
READFILE  = 1
FINDCAG   = 2
GCPERCENT = 3
EXIT      = 4
ERROR     = -1

# definition of the snip of DNA of interest
REPEAT    = "cag"

# constants for Classification Status


# ---------------------------

def getDNA(dnaFile):
    """ignoring header line, returns all DNA in file as one lowercase string; returns empty string if bad file"""

    DNA = ""
    if not os.path.exists(dnaFile):
        print("\nSORRY, the file", dnaFile, "does not exist.")
        print("Try another filename ...")

    else:
        line = 0
        FILE = open(dnaFile, 'r')
        print("Using file:", dnaFile)
        headerLine = FILE.readline() #isolates header so it isn't stored to DNA
        headerLine = headerLine.strip() #isolates header so it isn't stored to DNA
        #print(headerLine)
        for nextLine in FILE:
            nextLine = nextLine.strip() #reads lines
            freshDNA = nextLine #tracks the new line of DNA to add to total DNA string
            #print(nextLine)
            DNA = DNA + freshDNA #the total DNA string
            
            
            
        
            
                
        
            
        
        
    # end else
    print(DNA)

    return DNA
# ---------------------------------------------------------

def findCAGs(DNA):
    """report on all 'cag' repeats (lowercase) in a string of DNA"""

    #start looking in the string DNA at start(0) for cag-repeats
    DNAcags = DNA.lower() #converts DNA to lowercase for CAG locating
    where = DNAcags.find(REPEAT) #tracks position of CAGs located
    #cagCount = 0 #counts the amount of CAGs, also I didn't need it
    repeatCount = 0 #counts the amount of CAG repeats
    while (where != -1):
        #print("#", cagCount, "[position:", where, "]", DNAcags[where:])
        prevCag = where #tracks the position of the previous CAG for tracking purposes
        #print(prevCag)
        where = DNAcags.find(REPEAT, where + 1) #tracks current CAG
        #print(where)
        if (where - 3 == prevCag):
            print("CAG repeat at position:", prevCag)
            print(DNAcags[prevCag:])
            repeatCount = repeatCount + 1 #counts CAG repeats
    print("Total CAG repeats:", repeatCount)
    if(repeatCount <= 26):
        print("Classification: Normal. Unaffected by disease.")
    elif(repeatCount <= 35):
        print("Classification: Intermediate. Unaffected by disease.")
    elif(repeatCount <= 39):
        print("Classification: Reduced Penetrance. May be affected by disease.")
    elif(repeatCount > 39):
        print("Classification: Full Penetrance. Definitely affected by disease.")
            
            
        
        
    
           

           
           
    
# ---------------------------------------------------------

def getGCpercentage(DNA):
    """return the GC percentage of a strand of DNA"""
    dnaLength = len(DNA) #counts the length of the DNA string
    findG = DNA.count("G") #finds the letter G in DNA string
    findC = DNA.count("C") #finds the letter C in DNA string
    print(findG)
    print(findC)
    print(dnaLength)
    GCpercent = ((findC + findG)/dnaLength) * 100 #calculates percentage of Gs and Cs
    print("Percentage of G and C:"," %6.2f" % GCpercent)
    
    return getGCpercentage
    
        
# ---------------------------------------------------------

def main():

    gotDNA = False   # flag to tell if we've already loaded some DNA
    DNA = ""         # string of DNA held here

    choice = -1  # bogus setting to get us started

    while (choice != EXIT):
        print ("------------------------------")
        print ("  1  -  Read DNA file")
        print ("  2  -  Find", REPEAT, "repeat");
        print ("  3  -  Report percent GC");
        print ("  4  -  EXIT");
        print ("---------------------------")
        choice = input("ENTER: ")

        # trap bad user input
        if ( (str(READFILE) <= choice) and (choice <= str(EXIT)) ):
            # force to an integer, for example "1" to 1
            choice = eval(choice)
        else:
            badInput = choice
            # force to an integer to test below
            choice = ERROR;

        # ============ 1: READ DNA FILE =============================
        if ( choice == READFILE):
            dnaFile = input("Enter DNA filename: ")

            DNA = getDNA(dnaFile)

            if (DNA != ""):
                gotDNA = True
                print ("First 10 nucleotides in DNA file in one string is:\n", DNA[:10].lower())
            # end if

        # ============ 2: FIND CAG Repeats =============================
        elif (choice == FINDCAG):

            if (gotDNA):
                #start looking in the string DNA at start(0) for cag-repeats
                findCAGs(DNA)
            # end if gotDNA

            else:
                print ("You cannot search for CAGs at this time.")
                print ("Please open a file of DNA to search first.")
            # end else no file open yet


        # ============ 3: COMPUTE GC % =============================
        elif (choice == GCPERCENT):

            if (gotDNA):
                getGCpercentage(DNA)
            # end if gotDNA
            
            else:
                print ("You cannot compute GC % at this time.")
                print ("Please open a file of DNA to search first.")
            # end else no file open yet

        # ============ 4: EXIT =====================================
        elif (choice == EXIT):
            print ("Goodbye ...")

        # ============ ? HUH ? =====================================
        else:  # invalid input
            print ("ERROR: ", badInput, "is an invalid input. Try again.")

    # end WHILE input is not EXIT

    print ("\n\nDone.\n")
# end main


#-----------------------------------------------------

if __name__ == '__main__':
    main()

#-----------------------------------------------------
