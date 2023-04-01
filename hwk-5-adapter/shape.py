from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def setLocation(self):
        pass

    @abstractmethod
    def getLocation(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def fill(self):
        pass

    @abstractmethod
    def undisplay(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def getLocation(self):
        return self.x, self.y

    def display(self):
        print("Rectangle at ({}, {}) with width {} and height {}".format(
            self.x, self.y, self.width, self.height))

    def fill(self):
        print("Rectangle at ({}, {}) with width {} and height {} is filled".format(
            self.x, self.y, self.width, self.height))

    def undisplay(self):
        print("Rectangle at ({}, {}) with width {} and height {} is undisplayed".format(
            self.x, self.y, self.width, self.height))


class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def setLocation(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getLocation(self):
        return self.x1, self.y1, self.x2, self.y2

    def display(self):
        print("Line from ({}, {}) to ({}, {})".format(
            self.x1, self.y1, self.x2, self.y2))

    def fill(self):
        print("Line from ({}, {}) to ({}, {}) is filled".format(
            self.x1, self.y1, self.x2, self.y2))

    def undisplay(self):
        print("Line from ({}, {}) to ({}, {}) is undisplayed".format(
            self.x1, self.y1, self.x2, self.y2))


class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def getLocation(self):
        return self.x, self.y

    def display(self):
        print("Point at ({}, {})".format(self.x, self.y))

    def fill(self):
        print("Point at ({}, {}) is filled".format(self.x, self.y))

    def undisplay(self):
        print("Point at ({}, {}) is undisplayed".format(self.x, self.y))


class XXCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def getLocation(self):
        return self.x, self.y

    def displayIt(self):
        print("Circle at ({}, {}) with radius {}".format(
            self.x, self.y, self.radius))

    def fillIt(self):
        print("Circle at ({}, {}) with radius {} is filled".format(
            self.x, self.y, self.radius))

    def undisplayIt(self):
        print("Circle at ({}, {}) with radius {} is undisplayed".format(
            self.x, self.y, self.radius))

    def setItsColor(self, color):
        print("Circle at ({}, {}) with radius {} is filled with color {}".format(
            self.x, self.y, self.radius, color))


class CircleAdapter(XXCircle):
    def __init__(self, circle):
        self.circle = circle

    def setLocation(self, x, y):
        self.circle.setLocation(x, y)

    def getLocation(self):
        return self.circle.getLocation()

    def display(self):
        self.circle.displayIt()

    def fill(self):
        self.circle.fillIt()

    def undisplay(self):
        self.circle.undisplayIt()

    def setItsColor(self, color):
        self.circle.setItsColor(color)


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def getLocation(self):
        return self.x, self.y

    def display(self):
        print("Circle at ({}, {}) with radius {}".format(
            self.x, self.y, self.radius))

    def fill(self):
        print("Circle at ({}, {}) with radius {} is filled".format(
            self.x, self.y, self.radius))

    def undisplay(self):
        print("Circle at ({}, {}) with radius {} is undisplayed".format(
            self.x, self.y, self.radius))
