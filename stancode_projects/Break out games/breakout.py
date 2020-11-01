"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3 # the maximum times you can restart


def main():
    '''
    The ball will bounce when hit the paddle and bricks so bricks will be removed.
    If the ball comes out of the window, you lose. If all bricks were removed, you win.
    '''
    graphics = BreakoutGraphics()
    ball = graphics.get_ball() # the moving ball
    for i in range(NUM_LIVES): # the player can play 'NUM_LIVES' times
        while True:
            dx = graphics.get_dx() #the ball moves dx
            dy = graphics.get_dy() #the ball moves dy
            ball.move(dx,dy)
            graphics.window_border()
            graphics.bounce_ball()
            graphics.hit_brick()
            if graphics.is_win_game():
                break
            pause(FRAME_RATE)
            if graphics.move_to_bottom():
                break
        graphics.back_to_start()
    if graphics.is_win_game():
        graphics.win_game()
    else:
        graphics.end_game()



if __name__ == '__main__':
    main()
