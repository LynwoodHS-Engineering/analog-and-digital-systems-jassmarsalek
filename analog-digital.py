loop=1

while loop==1:
    value = encoder_a.position(DEGREES)
    motor_1.spin_for(FORWARD, 90, DEGREES)
    brain.screen.print_at((value), x=150, y=150)

    if bumper_c.pressing():
        break
