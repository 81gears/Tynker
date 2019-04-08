# Jungle Run
# Loops & Patterns

# Forward, Fire, Repeat

for i in range(8):
    fire()
    forward()

# Make a Zig-Zag
for i in range(5):
    forward()
    turn_right()
    forward()
    turn_left()

# March On

for i in range(4):
    forward()
turn_right()

for j in range(6):
    forward()

# Jump, Forward

for i in range(3):
    fire()
    jump()
    forward()

# Forward, Jump

for i in range(3):
    fire()
    forward()
    jump()

# Up and Down

for i in range(3):
    fire()
    forward()
    turn_left()
    turn_right()

jump()

for j in range(3):
    turn_right()
    fire()
    forward()
    turn_left()
    forward()

# U-Turn
# a nested loop

for i in range(3):
    # you need a second loop here
    for j in range(5):
        forward

    turn_left()    
    
