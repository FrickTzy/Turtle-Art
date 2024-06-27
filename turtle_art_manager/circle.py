from .turtle_art import TurtleArt
from turtle import Screen, Turtle


class Circle(TurtleArt):
    """
    A class representing a circle drawn using Turtle graphics.

    Attributes:
        radius (int): The radius of the circle.
    """

    def __init__(self, screen: Screen, pen: Turtle, radius: int, stroke_size: int = 5,
                 color: str = "black", position: tuple[int, int] = (0, 0), fill_color: str = "black"):
        """
        Initialize a Circle object.

        Args:
            screen (Screen): The turtle Screen object where the circle will be drawn.
            pen (Turtle): The Turtle object used to draw the circle.
            radius (int): The radius of the circle.
            stroke_size (int, optional): The thickness of the circle's outline. Defaults to 5.
            color (str, optional): The color of the circle's outline. Defaults to "black".
            position (tuple[int, int], optional): The starting position of the circle. Defaults to (0, 0).
            fill_color (str, optional): The fill color inside the circle. Defaults to "black".
        """
        super().__init__(screen=screen, pen=pen, position=position, color=color, stroke_size=stroke_size,
                         fill_color=fill_color)
        self._radius = radius

    def _draw_art(self) -> None:
        """
        Draw the circle on the screen.
        """
        self._go_to_position()
        self._pen.circle(self._radius)
