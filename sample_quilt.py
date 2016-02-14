#Hannah Weissman
#CS111 PSet Task 2
#February 1 2016
#sample_quilt.py

from picture import *

#Patch Function
def patch_2x2(c):
    """Returns a picture consisting of four rectangular patches of color c with black lines between the patches"""
    return (fourPics(patch(c), patch(c), patch(c), patch(c)))
    
#Triangle Function    
def triangles_2x2(c1, c2):
    """Returns two triangles each composed of two smaler triangles and a rectangle"""
    triangle1 = triangles(c1,c2)
    return (fourPics(triangle1, patch(c2), patch(c1), triangle1))

#Bandana Function
def bandana(c1, c2):
    """Returns a picture with a large lower left triangle of color c1, 
    two small triangles in the upper left and lower right corners of color c2,
    and a solid patch in the upper right corner of color c1. """
    pic1 = triangles_2x2(c1, c2) 
    pic2 = fourPics(empty(), patch(c1), empty(), empty())
    return overlay(pic2, pic1)

#Corner Function    
def corner(pic1, pic2):
    """Returns a picture which divides the picture space into four quadrants
    and places p1 in the lower left corner and p2 in the remaining three corners."""
    return fourPics(pic2, pic2, pic1, pic2)

#LL Function
def LL(pic1):
    """Returns a picture which divides the picture space into four quadrants 
    and places the given picture in the lower left corner."""
    return fourPics(empty(), empty(), pic1, empty())

#LLNest Function
def LLNest(pic1, pic2):
    """Returns a picture which places picture p2 over the lower left corner of picture p1."""
    picture2 = fourPics(empty(), empty(), pic2, empty())
    return overlay(picture2, pic1)
    
#UpperRightBlock Function
def upperRightBlock(c1, c2):
    """Returns the upper right block of the 2nd quadrant of the quilt"""
    pic1 = LL(triangles(c1,c2))
    pic2 = triangles(c1,c2)
    pic3 = fourPics(empty(), empty(), overlay(pic1, pic2), empty())
    pic4 = fourPics(empty(), empty(), overlay(pic3, pic2), empty())
    return overlay(pic4, pic2)
 
#UpperLeftBlock Function   
def upperLeftBlock(c1,c2,c3,c4,c5): #c1= royalblue c2=lightcyan2 c3=navy c4=lightskyblue c5=darkslateblue
    """Returns the upper left block of the 2nd quadrant of the quilt, this block
    is also the same as the lower right block of the 2nd quadrant"""
    pic1 = patch_2x2(c1)
    pic2 = bandana(c2,c3) 
    pic3 = bandana(c3,c4) 
    pic4 = triangles_2x2(c3,c4) 
    pic5 = triangles_2x2(c4,c5) 
    lowerLeftPic = fourPics(pic2, pic3, pic1, pic2) #lower left quadrant of the block
    upperLeftPic = fourPics(pic5, pic5, pic4, pic5) #upper left/lower right quadrant of the block
    upperRightPic = fourPics( pic5, pic5, pic5, pic5) #upper right quadrant of the block
    return fourPics(upperLeftPic, upperRightPic, lowerLeftPic, upperLeftPic)

#LowerLeftBlock Function
def lowerLeftBlock(c1,c2,c3,c4,c5): 
    """Returns the lower left block of the second quadrant of the quilt"""
    pic1 = fourPics(patch(c1), patch(c2), triangles(c5,c2), patch(c1))
    pic2 = triangles_2x2(c1, c5)
    pic3 = fourPics(patch(c5), patch(c2), patch(c2), patch(c5))
    lowerLeftPic = fourPics(pic2, pic3, pic1, pic2) # lower left quadrant of the block
    pic4 = patch_2x2(c1) 
    pic5 = patch_2x2(c5) 
    upperLeftPic = fourPics(pic5, pic5, pic4, pic4) #upper left quadrant of the block
    pic6 = bandana(c2,c3) 
    pic7 = bandana(c3,c4) 
    upperRightPic = fourPics(pic6, pic7, pic4, pic6) #upper right quadrant of the block
    lowerRightPic = fourPics(pic4, pic5, pic4, pic5) #lower right quadrant of the block
    return fourPics(upperLeftPic, upperRightPic, lowerLeftPic, lowerRightPic)
   
#UpperRightQuilt Function 
def upperRightQuilt(c1,c2,c3,c4,c5,c6): 
    """Returns upper right (2nd) quadrant of the whole quilt """
    pic1 = upperLeftBlock(c1,c2,c3,c4,c6) 
    pic2 = upperRightBlock(c6,c3)
    pic3 = lowerLeftBlock(c1,c2,c3,c4,c5)
    return fourPics(pic1 ,pic2, pic3, pic1)
    
#LowerRightQuilt Function
def lowerRightQuilt(pic1): #pic1= upperRightQuilt()
    """Returns the lower right quadrant of the whole quilt""" 
    result = pic1.clone()
    result.rotate(90)
    return result
    
#LowerLeftQuilt Function
def lowerLeftQuilt(pic1): #pic1 = upperRightQuilt()
    """Reurns the lower left quadrant of the whole quilt"""
    result = pic1.clone()
    result.rotate(180)
    return result

#UpperLeftQuilt Function
def upperLeftQuilt(pic1): #pic1 = upperRightQuilt()
    """Returns the upper left quadrant of the whole quilt"""
    result = pic1.clone()
    result.rotate(-90) #rotates 
    return result
    
#Quilt Function
def quilt(c1,c2,c3,c4,c5,c6):
    """Returns the entire quilt"""
    upperRight = upperRightQuilt(c1,c2,c3,c4,c5,c6)
    lowerRight = lowerRightQuilt(upperRight)
    lowerLeft = lowerLeftQuilt(upperRight)
    upperLeft = upperLeftQuilt(upperRight)
    return fourPics(upperLeft, upperRight, lowerLeft, lowerRight)
    
#Test Quilt: royalblue, lightcyan2, navy, lightskyblue, darkseagreen, darkslateblue
displayPic(quilt("royalblue", "lightcyan2", "navy", "lightskyblue", "darkseagreen", "darkslateblue"))

