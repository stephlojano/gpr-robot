from movement import  *

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

upper_left(100)
time.sleep(1)
stop_car()

lower_right(100)
time.sleep(1)
stop_car()

upper_right(100)
time.sleep(1)
stop_car()

lower_left(100)
time.sleep(1)
stop_car()

GPIO.cleanup()