from pygame import Vector2
class Cell:
    def __init__(self,
        name: str,
        rotation: int,
        position: Vector2
        ):
        if rotation in [0, 90, -90, 180]:
            self.data = {"name":name,"rotation":rotation,"pos":position}
        self.give(data=self.data)
    def give(self, data):
        return data