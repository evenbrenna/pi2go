import pi2go, time

pi2go.init()

speed = 40
LEDon = 4095
LEDoff = 0

try:
  while True:
    pi2go.setAllLEDs(LEDoff, LEDoff, LEDoff)
    if pi2go.irLeft():
      pi2go.setLED(0, LEDon, LEDoff, LEDoff)
      while pi2go.irLeft():
        pi2go.spinRight(speed)
      pi2go.stop()
    if pi2go.irRight():
      pi2go.setLED(2, LEDon, LEDoff, LEDoff)
      while pi2go.irRight():
        pi2go.spinLeft(speed)
      pi2go.stop()
    if pi2go.irCentre():
      pi2go.setLED(1, LEDon, LEDon, LEDon)
      while pi2go.irCentre():
        pi2go.reverse(speed)
        time.sleep(2)
        pi2go.spinRight(speed)
        time.sleep(1)
      pi2go.stop()
    while not (pi2go.irLeft() or pi2go.irRight() or pi2go.irCentre()):
      if pi2go.getDistance() <= 3.0:
        pi2go.spinRight(speed)
        time.sleep(2)
      else:
        pi2go.setAllLEDs(LEDoff, LEDoff, LEDoff)
        pi2go.setLED(3, LEDon, LEDon, LEDon)
        pi2go.forward(speed)
    pi2go.stop()

finally:
  pi2go.cleanup()
