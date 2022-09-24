class Rectangle:
  def __init__(self, width, height):
    self.height=height
    self.width=width

  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
  def set_width(self, width):
    self.width=width
    

  def set_height(self, height):
    self.height=height


  def get_area(self):
    return self.height*self.width

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
     

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
     

  def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

  def get_amount_inside(self, ob):
      return self.get_area() // ob.get_area()


  



class Square(Rectangle):
  def __init__(self, s):
    super().__init__(s, s)
    
  def __str__(self):
    return "Square(side="+str(self.width)+")"

  def set_side(self,side):
    self.height=side
    self.width=side
    
