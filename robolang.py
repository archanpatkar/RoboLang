from textx import metamodel_from_file
from Robot import Robot
from Robot import default

robotlang = metamodel_from_file('robot.tx')

robot_model = robotlang.model_from_file('one.rl')
robotlang.register_obj_processors({'MoveCommand': default})


r1 = Robot()

r1.interpret(robot_model);

input("Program Complete Press Enter to Close");