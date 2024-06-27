from .turtle_art import TurtleArt


class Rectangle(TurtleArt):
    """
    A class representing a rectangle drawn using Turtle graphics.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, *args, width: int = 100, height: int = 35, **kwargs):
        """
        Initialize a Rectangle object.

        Args:
            *args: Positional arguments passed to the superclass constructor (TurtleArt).
            width (int, optional): The width of the rectangle. Defaults to 100.
            height (int, optional): The height of the rectangle. Defaults to 35.
            **kwargs: Additional keyword arguments passed to the superclass constructor (TurtleArt).
        """
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

    def _draw_art(self) -> None:
        """
        Draw the rectangle on the screen.
        """
        self._go_to_position()
        for _ in range(2):
            self.pen.forward(self.width)
            self.pen.right(90)
            self.pen.forward(self.height)
            self.pen.right(90)
