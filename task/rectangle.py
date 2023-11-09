from dataclasses import dataclass


@dataclass
class Rectangle:  # I assumed that this is a 2D space
    x0: int  # X-coordinate of the top-Left corner
    y0: int  # Y-coordinate of the top-left corner
    x1: int  # X-coordinate of the bottom-right corner
    y1: int  # Y-coordinate of the bottom-right corner

    def contains(self, other: "Rectangle") -> bool:
        return (self.x0 <= other.x0 <= self.x1 and
                self.y0 <= other.y0 <= self.y1 and
                self.x0 <= other.x1 <= self.x1 and
                self.y0 <= other.y1 <= self.y1)

    def intersect(self, other: "Rectangle") -> bool:
        return (self.x0 < other.x1 and self.x1 > other.x0 and
                self.y0 < other.y1 and self.y1 > other.y0)
