from pico2d import load_image

class Grass:
    image = None
    def __init__(self, x = 400, y = 30):
        if Grass.image == None:
            Grass.image = load_image('grass.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
