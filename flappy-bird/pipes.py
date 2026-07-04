import pyray as rl

class Pipes:
    def __init__(self):
        self.pipes = []
        self.speed = -500
        # Pipes representation. Which I didn't followed..
        # [
        #    pos=[0,0]
        # ]

    def spawn(self, x, y):
        self.pipes.append([x,y])

    def reset(self):
        self.pipes = []

    def update(self, dt):
        for i in range(len(self.pipes) - 1, -1, -1):
            pipe = self.pipes[i]
            pipe[0] += self.speed * dt
            if pipe[0] < -100:
                self.pipes.pop(i)

    def draw(self):
        for pipe in self.pipes:
            # Shit so doggy water
            rl.draw_rectangle(
                int(pipe[0]),
                int(pipe[1])-700,
                100,
                800,
                rl.GREEN
            )
            rl.draw_rectangle(
                int(pipe[0]),
                int(pipe[1])+350,
                100,
                800,
                rl.GREEN
            )
