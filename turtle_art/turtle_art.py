from turtle import Screen, Turtle
from .turtle_draw import TurtleDraw
from abc import ABC, abstractmethod


class TurtleArt(ABC, TurtleDraw):
    """
    Abstract base class for turtle-based artistic drawings.

    Attributes:
        position (tuple[int, int]): The starting position of the drawing.
        fill_color (str): The fill color used when filling shapes.
    """

    def __init__(self, screen: Screen, pen: Turtle, position: tuple[int, int] = (0, 0),
                 stroke_size: int = 5, color: str = "black", fill_color: str = "black"):
        """
        Initialize a TurtleArt object.

        Args:
            screen (Screen): The turtle Screen object where drawing occurs.
            pen (Turtle): The Turtle object used for drawing operations.
            position (tuple[int, int], optional): The starting position of the drawing. Defaults to (0, 0).
            stroke_size (int, optional): The thickness of the drawing pen. Defaults to 5.
            color (str, optional): The color of the drawing pen. Defaults to "black".
            fill_color (str, optional): The fill color used when filling shapes. Defaults to "black".
        """
        super().__init__(screen=screen, pen=pen, stroke_size=stroke_size, color=color)
        self.position = position
        self.fill_color = fill_color

    def _go_to_position(self) -> None:
        """
        Move the pen to the specified drawing position.
        """
        self._go_to(self.position)

    def _go_to(self, position: tuple[int, int]) -> None:
        """
        Move the pen to a specified position.

        Args:
            position (tuple[int, int]): The position to move to.
        """
        self.pen.penup()
        self.pen.goto(position)
        self.pen.pendown()

    def _draw_to(self, position: tuple[int, int]) -> None:
        """
        Draw a line to a specified position.

        Args:
            position (tuple[int, int]): The position to draw to.
        """
        self.pen.pendown()
        self.pen.goto(position)
        self.pen.penup()

    def draw(self, fill_color: bool = False) -> None:
        """
        Draw the artistic shape.

        Args:
            fill_color (bool, optional): Whether to fill the shape with fill_color. Defaults to False.
        """
        if fill_color:
            self.pen.fillcolor(self.fill_color)
            self.pen.begin_fill()
        self._set_pen_stroke()
        self._draw_art()
        if fill_color:
            self.pen.end_fill()

    @abstractmethod
    def _draw_art(self) -> None:
        """
        Abstract method to be implemented by subclasses to define the drawing logic.
        """
        pass
