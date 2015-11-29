import pi2go, time

pi2go.init()

speed = 40

try:
  while True:
    if pi2go.irLeft():
      while pi2go.irLeft():
        pi2go.spinRight(speed)
      pi2go.stop()
    if pi2go.irRight():
      while pi2go.irRight():
        pi2go.spinLeft(speed)
      pi2go.stop()
    if pi2go.irCenter():
      while pi2go.irCenter():
        pi2go.reverse(speed)
        time.sleep(2)
        pi2go.spinRight(speed)
        time.sleep(1)
      pi2go.stop()
    while not (pi2go.irLeft() or pi2go.irRight() or pi2go.irCenter()):
      if pi2go.getDistance() <= 3.0:
        pi2go.spinRight(speed)
        time.sleep(1)
      else:
        pi2go.forward(speed)
    pi2go.stop()

finally:
  pi2go.cleanup()
