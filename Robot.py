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
            elif c.__class__.__name__ == "MoveCommand":
                dir = c.direction
                print("Going {} for {} step(s).".format(dir, c.steps))
                if(dir == "up"):
                    self.x += c.steps * 0
                    self.y += c.steps * 1
                    self.turtle.setx(self.x)
                    self.turtle.sety(self.y)
                elif(dir == "down"):
                    self.x += c.steps * 0
                    self.y += c.steps * -1 
                    self.turtle.setx(self.x)
                    self.turtle.sety(self.y)
                elif(dir == "left"):
                    self.x += c.steps * -1
                    self.y += c.steps * 0
                    self.turtle.setx(self.x)
                    self.turtle.sety(self.y)
                elif(dir == "right"):
                    self.x += c.steps * 1
                    self.y += c.steps * 0
                    self.turtle.setx(self.x)
                    self.turtle.sety(self.y)
            elif c.__class__.__name__ == "GoToCommand":
                self.x = c.x
                self.y = c.y
                self.turtle.penup()
                self.turtle.setx(self.x)
                self.turtle.sety(self.y)
                self.turtle.pendown()
            elif c.__class__.__name__ == "CircleCommand":
                self.turtle.circle(c.radius)
            elif c.__class__.__name__ == "DotCommand":
                self.turtle.dot(c.size)
            time.sleep(1)