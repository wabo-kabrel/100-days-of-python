# The Hurdles Loop Challenge

direction = 0 

def move():
    global direction         # The keyword global tells Python that the direction used inside move() refers to the variable defined outside the function.
    direction = direction + 1
    

def turn_left():
    global direction
    direction = direction - 1
    

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

def turn_right():
    for step in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

