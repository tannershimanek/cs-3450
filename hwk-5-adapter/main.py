from shape import Rectangle, Line, CircleAdapter, XXCircle


def main():
    rect = Rectangle(10, 20, 30, 40)
    rect.display()

    line = Line(100, 200, 300, 400)
    line.display()

    circle = CircleAdapter(XXCircle(100, 200, 50))
    circle.display()


if __name__ == "__main__":
    main()
