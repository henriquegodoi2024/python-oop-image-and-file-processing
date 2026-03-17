

import math
   
class Rectangle:
    def __init__(self, init_width, init_height, init_unit):
        """ constructor for a Rectangle object with the specified dimensions 
            init_width and init_height, and initial x and y coordinates of 0
        """
        self.x = 0
        self.y = 0
        self.width = init_width
        self.height = init_height
        self.unit = init_unit
    
    def grow(self, dwidth, dheight):
        """ modifies the dimensions of the called Rectangle object
            (the one given by self) by adding dwidth to the current width
            and dheight to the current height.
            Note that nothing needs to be returned. The changes are
            made to the internals of the called object, and thus they 
            will still be there after the method returns!
        """
        self.width += dwidth
        self.height += dheight

    def area(self):
        """ computes and returns the area of the called Rectangle object
        """
        return self.width * self.height

    def perimeter(self):
        """ computes and returns the perimeter of the called Rectangle object
        """
        return 2*self.width + 2*self.height

    def scale(self, factor):
        """ modifies the dimensions of the called Rectangle object
            by multiplying them by the specified factor.
        """
        self.width *= factor
        self.height *= factor

    def __eq__(self, other):
        """ determines if the called Rectangle object (self) is 
            equivalent to the Rectangle object given by other
            note: the \ symbol at the end of the first line below 
            allows us to continue that line onto the next line of the file.
        """
        if self.width == other.width and \
           self.height == other.height and \
           self.unit == other.unit:
            return True
     
        else:
            return False

    def __repr__(self):
        """ creates and returns a string representation of the 
            called Rectangle object
        """
        return str(self.width) + ' x ' + str(self.height) + ' ' + str(self.unit)
    
    def diagonal(self):
        ''' returns the square root of the width and height 
        of the rectangle object'''
        return math.sqrt(self.width**2 + self.height**2)
    
    def larger_than(self,other):
        ''' takes the parameter other and compares to the self object
        returning True if the area of self is greater than the area
        of other'''
        if (self.width * self.height) > (other.height * other.width):
            return True
        else:
            return False
    
