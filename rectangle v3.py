class Rectangle:
    def __init__(self, height: float, width: float):
        # Initialize a Rectangle object with height and width attributes.
        self._height = height  # Assign the height attribute
        self._width = width    # Assign the width attribute

    @property
    def height(self):
        # Getter method for retrieving the height attribute
        return self._height

    @property
    def width(self):
        # Getter method for retrieving the width attribute
        return self._width

    @height.setter
    def height(self, newheight):
        # Setter method for modifying the height attribute
        if newheight >= 0:
            self._height = newheight  # Update height if the new value is non-negative
        else:
            print(f"New height value should not be below 0")  # Display error message for negative input

    @width.setter
    def width(self, newwidth):
        # Setter method for modifying the width attribute
        if newwidth >= 0:
            self._width = newwidth  # Update width if the new value is non-negative
        else:
            print(f"New width value should not be below 0")  # Display error message for negative input

    def area(self):
        # Method to calculate the area of the rectangle
        return self.height * self.width

    def perimeter(self):
        # Method to calculate the perimeter of the rectangle
        return 2 * (self.height * self.width)

# Create an instance of the Rectangle class with height=6 and width=2
obj = Rectangle(height=6, width=2)

# Uncomment these lines to test negative values (not allowed by the setter methods)
# obj.height = -5
# obj.width = -2

# Modify the height and width attributes using the setter methods
obj.height = 5
obj.width = 3

# Display the calculated area and perimeter of the rectangle
print(f"Area: {obj.area()}")
print(f"Perimeter: {obj.perimeter()}")
