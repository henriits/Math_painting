
class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        pass
class Square:
    def __init__(self,x ,y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pass
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self,canvas):
        pass


canvas_width = int(input("Enter a canvas width: "))
canvas_height = int(input("Enter a canvas height: "))
canvas_color = input("Enter canvas color (white or black): ")
object_to_draw = input("what do you like to draw? Enter quit to quit. ")  # while true
object_x_location = int(input(f"Enter x of {object_to_draw}"))
object_y_location = int(input(f"Enter x of {object_to_draw}"))
object_width = input(f"Enter the width of the {object_to_draw}")
object_height = input(f"Enter the height of the {object_to_draw}")
red = input("How much red should the rectangle have? ")
green = input("How much green should the rectangle have? ")
blue = input("How much blue should the rectangle have? ")
