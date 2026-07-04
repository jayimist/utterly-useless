import pyray as rl

class Player:
    def __init__(self):
        self.reset()
        self.size = [70,70]
        self.color = rl.Color(255, 249, 61, 255)
        self.gravity = 60
        self.flappower = -850

    def reset(self):
        self.pos = [100,800/2]
        self.vel = [0,0]

    def update(self, dt):
        self.vel[1] += self.gravity

        if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE) or rl.is_key_pressed(rl.KeyboardKey.KEY_W) or rl.is_mouse_button_down(rl.MouseButton.MOUSE_BUTTON_LEFT):
            self.vel[1] = self.flappower

        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt

    def draw(self):
        rl.draw_rectangle(int(self.pos[0]),int(self.pos[1]),self.size[0],self.size[1],self.color)

