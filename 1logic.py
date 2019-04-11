# Conditional logic if,elif,else

# Path Right

for i in range(9):
    if has_path_right():
        turn_right()
     
    forward()

#________________________

#Path Left

for j in range(7):
    if has_path_left():
        turn_left()
        fire()

    forward()
    



# More Turns

for g in range(10):
    if has_path_right():
        turn_right()
    if has_path_left():
        turn_left()

    forward()    



# Hazardous Path

for i in range(10):
    if has_path_right():
        turn_right()
    if has_path_left():
        turn_left()
    if enemy_in_sight():
        fire()
    forward()    
        

# Death Valley

for j in range(22):
    if enemy_in_sight():
        fire()
    elif(has_path_left()):
        turn_left()
    forward()  
        



# Traps

for i in range(24):
    if has_path_right():
        turn_right()
        forward()
    elif has_path_left():
        turn_left()
        forward()
    elif is_gap_ahead():
        jump()
    else:
        forward()
    



# G for Grandeur

for h in range(13):
    if has_path_left():
        turn_left()
        forward()
    elif is_gap_ahead():
        jump()
    else:
        forward()
    

# Silly Path

for i in range(18):
    if has_path_left():
        turn_left()
        forward()
    elif has_path_right():
        turn_right()
        forward()
    elif is_gap_ahead():
        jump()
    else:
        forward()
        
    
