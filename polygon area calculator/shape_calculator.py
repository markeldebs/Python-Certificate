class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.heigh = height
        
    def set_width (self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
    
    
    def get_area(self): 
        # Returns area (width * height)
        return (self.width * self.height)
    
    def get_perimeter(self):
        # Returns perimeter (2 * width + 2 * height)
        return (2* self.width + 2 * self.height)
    
    
    def get_diagonal(self):
        # Returns diagonal ((width ** 2 + height ** 2) ** .5)
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        
    
class Square:
    