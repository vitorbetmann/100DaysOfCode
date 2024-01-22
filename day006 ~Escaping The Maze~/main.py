#solution for the maze challenge at :
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if is_facing_north() and not front_is_clear() and not wall_on_right():
        turn_right()
    elif not front_is_clear() and wall_on_right():
        turn_left()
    elif not front_is_clear() and not wall_on_right():
        turn_right()
    else:
        move()
        if not wall_on_right():
            turn_right()
        
