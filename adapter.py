
# Target Interface: The interface your client expects.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a rectangle of width {self.width} and height {self.height}")


# Adaptee: The existing class with an incompatible interface.
class LegacyRectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def old_draw(self):
        print(f"Drawing a legacy rectangle from ({self.x}, {self.y}) with width {self.w} and height {self.h}")

# Adapter: The class that makes LegacyRectangle compatible with Rectangle.
class RectangleAdapter:
    def __init__(self, legacy_rectangle):
        self.legacy_rectangle = legacy_rectangle

    def draw(self):
        # Convert the interface
        self.legacy_rectangle.old_draw()


# Client: The code that uses the Rectangle interface
# Original client code using Rectangle
rect = Rectangle(10, 20)
rect.draw()  # Outputs: Drawing a rectangle of width 10 and height 20

# Using the Adapter to make LegacyRectangle compatible with Rectangle
legacy_rect = LegacyRectangle(0, 0, 10, 20)
adapted_rect = RectangleAdapter(legacy_rect)
adapted_rect.draw()  # Outputs: Drawing a legacy rectangle from (0, 0) with width 10 and height 20




# How It Works:
# Target Interface (Rectangle): Defines the methods the client expects.
# Adaptee (LegacyRectangle): Has a different interface that needs to be adapted.
# Adapter (RectangleAdapter): Implements the target interface and translates the calls to the adaptee’s methods.
# This way, the client can use the LegacyRectangle through the RectangleAdapter without any changes to the original LegacyRectangle or client code, providing a flexible and reusable solution for compatibility issues.
