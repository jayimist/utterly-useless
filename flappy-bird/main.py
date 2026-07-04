import pyray as rl
import os, random

rl.init_window(600, 800, "Flappy Bird")
rl.set_target_fps(60)

GAME_STATE = "start"
spawn_pipe_threshold = 1
pipe_timer = spawn_pipe_threshold

from player import Player; player = Player()
from pipes import Pipes; pipes = Pipes()



def game_over():
    global GAME_STATE
    player.reset()
    pipes.reset()
    GAME_STATE = "start"

def rects_collide(x1, y1, w1, h1, x2, y2, w2, h2):
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )

# MAX/MIN PIPE LEVEL 0/350
# pipes.spawn(600, 0)

while not rl.window_should_close():
    os.system("clear")
    dt = rl.get_frame_time()
    print(f"Flappy Bird • Jayimist\nwindow info:\ndt: {dt}\nfps: {rl.get_fps()}\n\npipe info:\npipes: {len(pipes.pipes)}\npipe timer: {pipe_timer}\nspawn pipe threshold: {spawn_pipe_threshold}\n\nplayer info:\npos: {player.pos[0]}, {player.pos[1]}\nvel: {player.vel[0]}, {player.vel[1]}")

    if GAME_STATE == "start":
        rl.begin_drawing()
        rl.clear_background(rl.Color(28, 104, 212, 255))

        player.draw()
        rl.draw_text("Press Space to flap!", 150, 400, 35, rl.WHITE)

        rl.end_drawing()

        if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE):
            GAME_STATE = "main"

    elif GAME_STATE == "main":
        for pipe in pipes.pipes:
            px = pipe[0]
            py = pipe[1]

            # TOP PIPE
            if rects_collide(
                player.pos[0], player.pos[1],
                player.size[0], player.size[1],
                px, py - 700,
                100, 800
            ):
                game_over()

            # BOTTOM PIPE
            if rects_collide(
                player.pos[0], player.pos[1],
                player.size[0], player.size[1],
                px, py + 350,
                100, 800
            ):
                game_over()
        player.update(dt)

        pipe_timer += 1 * dt
        if pipe_timer > spawn_pipe_threshold:
            pipe_timer = 0
            pipes.spawn(600, random.randint(0, 350))
        pipes.update(dt)

        if player.pos[1] < 0 or player.pos[1] > 800:
            game_over()

        rl.begin_drawing()
        rl.clear_background(rl.Color(28, 104, 212, 255))

        player.draw()
        pipes.draw()

        rl.end_drawing()


rl.close_window()

