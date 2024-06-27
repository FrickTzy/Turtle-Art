# Turtle-Art-Manager

The Turtle-Art-Manager package provides Python classes for creating artistic drawings using Turtle graphics.

## Installation

You can install the Turtle-Art package using pip:

```bash
pip install turtle-art-manager
```

## Classes

### TurtleArt Class

The `TurtleArt` class serves as an abstract base class for creating various artistic shapes using Turtle graphics.

#### Usage

```python
from turtle import Screen, Turtle
from turtle_art_manager import TurtleArt


class MyArt(TurtleArt):
    def _draw_art(self) -> None:
        pass


# Example usage:
screen = Screen()
pen = Turtle()
artwork = MyArt(screen, pen)
artwork.draw()
screen.mainloop()
```

#### Methods

- **draw()**: Draws the artistic shape on the screen.

### Rectangle Class

The `Rectangle` class is a subclass of `TurtleArt` that allows you to draw rectangles on the screen.

#### Usage

```python
from turtle import Screen, Turtle
from turtle_art_manager import Rectangle

# Example usage:
screen = Screen()
pen = Turtle()
rectangle = Rectangle(screen, pen, width=150, height=80)
rectangle.draw(fill_color=True)
screen.mainloop()
```

### Circle Class

The `Circle` class is another subclass of `TurtleArt` that allows you to draw circles on the screen.

#### Usage

```python
from turtle import Screen, Turtle
from turtle_art_manager import Circle

# Example usage:
screen = Screen()
pen = Turtle()
circle = Circle(screen, pen, radius=50)
circle.draw(fill_color=True)
screen.mainloop()
```

#### Attributes

- **width** (int): Width of the rectangle.
- **height** (int): Height of the rectangle.

