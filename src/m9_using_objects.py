"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Evan Cochrane.
"""  # 1. DONE PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(600, 600)

    circle1 = rg.Circle(rg.Point(200, 100), 75)
    circle1.fill_color = 'green'

    circle1.attach_to(window)

    circle2 = rg.Circle(rg.Point(350, 300), 150)
    circle2.outline_color = 'blue'

    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # 3. DONE Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------

    window = rg.RoseWindow(600,600)

    circle = rg.Circle(rg.Point(100, 100), 80)
    circle.outline_thickness = 15
    circle.fill_color = 'blue'
    circle.attach_to(window)

    print(15)
    print('blue')
    print('Point(100, 100)')
    print(100)
    print(100)
    print()

    window.render(3)

    rectangle = rg.Rectangle(rg.Point(100, 100), rg.Point(300, 400))
    rectangle.outline_thickness = 10
    rectangle.attach_to(window)

    window.render()

    print(10)
    print('None')
    print('Point(200, 250)')
    print(200)
    print(250)

    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # 4: DONE Implement and test this function.

    window = rg.RoseWindow()

    line1 = rg.Line(rg.Point(50, 100), rg.Point(125, 175))
    print(line1.get_midpoint())
    print(87.5)
    print(137.5)
    line1.attach_to(window)

    window.render(3)

    line2 = rg.Line(rg.Point(120, 60), rg.Point(300, 40))
    line2.thickness = 15
    print(line2.get_midpoint())
    print(210)
    print(50)
    line2.attach_to(window)

    window.render()

    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
