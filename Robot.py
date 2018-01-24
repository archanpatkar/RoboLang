import turtle
import time

def default(command):
    if command.steps == 0:
        command.steps = 1

class Robot:
    def __init__(self):
        self.x = 0;
        self.y = 0;
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.shapesize(1, 1, 2)

    def interpret(self, model):
        for c in model.commands:

            if c.__class__.__name__ == "InitialCommand":
                self.x = c.x
                self.y = c.y
                self.turtle.setpos(self.x,self.y)
            else:
                dir = c.direction
                print("Going {} for {} step(s).".format(dir, c.steps))

                move = {
                    "up": (0, 1),
                    "down": (0, -1),
                    "left": (-1, 0),
                    "right": (1, 0)
                }[dir]

                # Calculate new robot position
                self.x += c.steps * move[0]
                self.y += c.steps * move[1]

            self.turtle.setx(self.x)
            self.turtle.sety(self.y)
            time.sleep(1)