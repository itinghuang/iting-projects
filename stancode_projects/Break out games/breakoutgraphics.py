"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

# constants that cannot be changed by user
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.

count = 0 # the Qty of removed bricks


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(PADDLE_WIDTH,PADDLE_HEIGHT,x=(window_width/2-PADDLE_WIDTH/2),y=window_height-PADDLE_OFFSET)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball,x=(window_width/2-BALL_RADIUS), y=window_height/2-PADDLE_OFFSET)
        # Initialize our mouse listeners.
        onmouseclicked(self.ball_start)
        onmousemoved(self.paddle_move)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        # Default the removed bricks
        self.count = 0
        # Draw bricks.
        for j in range(BRICK_ROWS):
            for i in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x= (BRICK_WIDTH+brick_spacing)*i, y=BRICK_OFFSET+(BRICK_HEIGHT+brick_spacing)*j)
                self.brick.filled = True
                if j == 0 :
                    self.brick_color = 'red'
                elif j == 2:
                    self.brick_color = 'orange'
                elif j == 4:
                    self.brick_color = 'yellow'
                elif j == 6:
                    self.brick_color = 'green'
                elif j ==8:
                    self.brick_color = 'blue'
                self.brick.fill_color = self.brick_color
                self.brick.color = self.brick_color
                self.window.add(self.brick)

    def paddle_move(self, event):
        '''
        To set the remove paddle. The paddle will follow the position of mouse
        :return: the x of paddle
        '''
        self.paddle.x = event.x
        self.paddle.y = self.window.height-PADDLE_OFFSET
        if event.x <= 0:
            self.paddle.x = 0
        elif event.x >= (self.window.width-self.paddle.width):
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x

    def ball_start(self, event):
        '''
        If user click the mouse, the moving distance will increase (__dx, __dy) and start the moving.
        :return: new __dx, __dy
        '''
        if self.__dy == 0 and self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random > 0.5:
                self.__dx = -self.__dx
            if random.random > 0.5:
                self.__dy = -self.__dy

    def window_border(self):
        '''
        If the ball moved out of the window, the ball will bounce.
        :return: new __dx, __dy
        '''
        if self.ball.x <= 0 or self.ball.x >= (self.window.width-BALL_RADIUS*2):
            self.__dx = -self.__dx
        elif self.ball.y <= 0:
            self.__dy = -self.__dy

    def move_to_bottom(self):
        '''
        If the ball touched the bottom
        :return: boolean (True/False)
        '''
        if self.ball.y >= (self.window.height-BALL_RADIUS*2):
            return True

    def back_to_start(self):
        '''
        The ball moves back to the start point to restart the game.
        :return: ball.x , ball.y , __dx, __dy
        '''
        self.ball.x = self.window.width/2-BALL_RADIUS
        self.ball.y = self.window.height/2 - BALL_RADIUS
        self.__dx = 0
        self.__dy = 0

    def bounce_ball(self):
        '''
        if the ball hits the paddle, the ball will bounce.
        :return: new __dy
        '''
        x = self.ball.x
        y = self.ball.y
        obj = self.window.get_object_at(x, y)
        obj2 = self.window.get_object_at(x+2*BALL_RADIUS, y)
        obj3 = self.window.get_object_at(x, y+2*BALL_RADIUS)
        obj4 = self.window.get_object_at(x+2*BALL_RADIUS, y+2*BALL_RADIUS)
        if obj3 == self.paddle:
            self.__dy = -self.__dy
        elif obj4 == self.paddle:
            self.__dy = -self.__dy
        elif obj == self.paddle:
            self.__dy = -self.__dy
        elif obj2 == self.paddle:
            self.__dy = -self.__dy

    def hit_brick(self):
        '''
        If the ball hits the brick, the ball will bounce and the brick will be removed.
        :return: count, __dy, removed bricks
        '''
        obj4 = self.window.get_object_at(self.ball.x,self.ball.y)
        obj5 = self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y)
        obj6 = self.window.get_object_at(self.ball.x, self.ball.y+2*BALL_RADIUS)
        obj7 = self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y+2*BALL_RADIUS)
        if obj4 != self.paddle and obj4 != None:
            self.window.remove(obj4)
            self.count += 1
            self.__dy = -self.__dy
        elif obj5 != self.paddle and obj5 != None:
            self.__dy = -self.__dy
            self.count += 1
            self.window.remove(obj5)
        elif obj6 != self.paddle and obj6 != None:
            self.__dy = -self.__dy
            self.count += 1
            self.window.remove(obj6)
        elif obj7 != self.paddle and obj7 != None:
            self.__dy = -self.__dy
            self.count += 1
            self.window.remove(obj7)

    def is_win_game(self):
        '''
        If the game removed all the bricks
        :return: boolean (True/False)
        '''
        if self.count == BRICK_ROWS*BRICK_COLS:
            return True

    def win_game(self):
        '''
        If win, the game will over and the win-banner will appear.
        :return: sign2, label2
        '''
        sign2 = GRect(self.window.width, self.window.height, x=0, y=0)
        sign2.filled = True
        sign2.color = 'yellow'
        sign2.fill_color = 'yellow'
        self.window.add(sign2)
        label2 = GLabel('You win !', x=self.window.width/3.5, y=self.window.height/2)
        label2.font = 'Helvetica-35'
        label2.color = 'black'
        self.window.add(label2)

    def end_game(self):
        '''
        If lose, the game will over and the lose-banner will appear.
        :return: sign, label
        '''
        sign = GRect(self.window.width, self.window.height, x=0, y=0)
        sign.filled = True
        sign.color = 'red'
        sign.fill_color = 'red'
        self.window.add(sign)
        label = GLabel('You lose', x=self.window.width/3.5, y=self.window.height/2)
        label.font = 'Helvetica-35'
        label.color = 'black'
        self.window.add(label)
















    # Getter
    def get_dx(self):
        return self.__dx

    # Getter
    def get_dy(self):
        return self.__dy

    # Getter
    def get_ball(self):
        return self.ball









