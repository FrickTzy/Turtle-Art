from turtle import Screen, Turtle


class TurtleDraw:
    """
    A class for managing turtle drawing operations.

    Attributes:
        screen (Screen): The turtle Screen object.
        pen (Turtle): The Turtle object used for drawing.
        stroke_size (int, optional): The thickness of the drawing pen. Defaults to 5.
        color (str, optional): The color of the drawing pen. Defaults to "black".
    """

    def __init__(self, screen: Screen, pen: Turtle, stroke_size: int = 5, color: str = "black"):
        """
        Initialize a TurtleDraw object.

        Args:
            screen (Screen): The turtle Screen object where drawing occurs.
            pen (Turtle): The Turtle object used for drawing operations.
            stroke_size (int, optional): The thickness of the drawing pen. Defaults to 5.
            color (str, optional): The color of the drawing pen. Defaults to "black".
        """
        self._pen = pen
        self._screen = screen
        self._stroke_size = stroke_size
        self._color = color

    def _set_pen_stroke(self) -> None:
        """
        Set the stroke size of the drawing pen.
        """
        self._pen.pensize(self._stroke_size)
