from canvas import Canvas, Square, Rectangle

# canvas = Canvas(height=20,width=30,color=(255,255,255))
# r1 = Rectangle(x=1,y=6,height=7,width=10,color=(100,200,125))
# r1.draw(canvas)
# s1 = Square(x=1,y=3,side=3,color=(0,100,222))
# s1.draw(canvas)
# canvas.make("canvas1.png")

want_to_draw = True
while want_to_draw:
    canvas_width = int(input("Enter a canvas width: "))
    canvas_height = int(input("Enter a canvas height: "))
    canvas_color = input("Enter canvas color (white or black): ")
    object_to_draw = input("what do you like to draw? Enter quit to quit. ")  # while true
    if object_to_draw == "quit":
        break
    object_x_location = int(input(f"Enter x of {object_to_draw}: "))
    object_y_location = int(input(f"Enter x of {object_to_draw}: "))
    object_width = int(input(f"Enter the width of the {object_to_draw}: "))
    object_height = int(input(f"Enter the height of the {object_to_draw}: "))
    red = int(input("How much red should the rectangle have?: "))
    green = int(input("How much green should the rectangle have?: "))
    blue = int(input("How much blue should the rectangle have?: "))

    if canvas_color == "white":
        canvas_color = (255, 255, 255)
    elif canvas_color == "black":
        canvas_color = (0, 0, 0)
    canvas = Canvas(height=canvas_height, width=canvas_width, color=canvas_color)
    if object_to_draw == "quit":
        exit()
    elif object_to_draw == "rectangle":

        r1 = Rectangle(x=object_x_location, y=object_y_location, height=object_height, width=object_width,
                       color=(red, green, blue))
        r1.draw(canvas)

    elif object_to_draw == "square":
        s1 = Square(x=object_x_location, y=object_y_location, side=object_height, color=(red, green, blue))
        s1.draw(canvas)

    canvas.make("canvas1.png")
