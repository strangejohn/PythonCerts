import math
class Rectangle:
    #sets up rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #allows change to width
    def set_width(self, width):
        self.width = width

    #allows change to height
    def set_height(self, height):
        self.height = height

    #returns total area
    def get_area(self):
        return self.height * self.width

    #returns length of perimeter
    def get_perimeter(self):
        return (self.height * 2) + (self.width * 2)

    #returns length of diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    #created a pic of ***** to make shape baised on size
    def get_picture(self):
        count_right = self.width
        count_down = self.height
        counter = 0
        pic = ''
        if self.width > 50:
            return "Too big for picture."
        if self.height > 50:
            return "Too big for picture."
        while counter < count_down:
            pic += count_right*'*'
            pic += '\n'
            counter += 1
        return pic

    #creates new shape /// tests how many of current shape can fit into new shape
    def get_amount_inside(self, inside_shape):
        num_of_width = math.floor(self.width / inside_shape.width)
        num_of_height = math.floor(self.height / inside_shape.height)
        total_num_shape = num_of_width * num_of_height
        return total_num_shape


    #output string in accordance to guideline for shape
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    #import Rectangle class to set width and height to input vals
    def __init__(self, length):
        Rectangle.width = length
        Rectangle.height = length

    #import set_width/height to set sides
    def set_side(self, sides):
        Rectangle.set_width(self, sides)
        Rectangle.set_height(self, sides)

    #output string in accordance to guideline for shape
    def __str__(self):
        return "Square(side={})".format(self.width)
