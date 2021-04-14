import movement

go_ahead(100)
time.sleep(1)
stop_car()

go_back(100)
time.sleep(1)
stop_car()

turn_left(100)
time.sleep(1)
stop_car()

turn_right(100)
time.sleep(1)
stop_car()

shift_right(100)
time.sleep(1)
stop_car()

shift_left(100)
time.sleep(1)
stop_car()

change_duty_cycle(50)

go_ahead(100)
time.sleep(1)
stop_car()

go_back(100)
time.sleep(1)
stop_car()

turn_left(100)
time.sleep(1)
stop_car()

turn_right(100)
time.sleep(1)
stop_car()

shift_right(100)
time.sleep(1)
stop_car()

shift_left(100)
time.sleep(1)
stop_car()

GPIO.cleanup()
