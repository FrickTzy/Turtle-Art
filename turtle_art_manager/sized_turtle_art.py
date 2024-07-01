from .turtle_art import TurtleArt
from abc import ABC, abstractmethod


class SizedTurtleArt(TurtleArt, ABC):
    """
    An abstract base class for creating size-scaled artistic shapes using Turtle graphics.

    Attributes:
        _size (float): The scale size for the drawing.
    """

    def __init__(self, *args, size: float = 1, **kwargs):
        """
        Initialize a SizedTurtleArt object.

        Args:
            *args: Positional arguments passed to the superclass constructor (TurtleArt).
            size (float, optional): The scale size for the drawing. Defaults to 1.
            **kwargs: Additional keyword arguments passed to the superclass constructor (TurtleArt).
        """
        super().__init__(*args, **kwargs)
        self._size = size

    @abstractmethod
    def _draw_art(self) -> None:
        """
        Abstract method to be implemented by subclasses to define the drawing logic.
        """
        pass

    def _get_position(self, position: tuple[int, int]) -> tuple[int, int]:
        """
        Calculate a scaled position based on the given position and the size attribute.

        Args:
            position (tuple[int, int]): The original position to be scaled.

        Returns:
            tuple[int, int]: The scaled position.
        """
        return self._position[0] + int(position[0] * self._size), self._position[1] + int(position[1] * self._size)

    def _get_size(self, size: int) -> int:
        """
        Calculate a scaled size based on the given size and the size attribute.

        Args:
            size (int): The original size to be scaled.

        Returns:
            int: The scaled size.
        """
        return int(size * self._size)
