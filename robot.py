import pi2go, time, thread

pi2go.init()
pi2go.cleanup()

speed = 40
LEDon = 4095
LEDoff = 0

def ufoLights():
    while True:
        for i in range(4):
            pi2go.setLED(i, 4095, 0, 0) # set to Red
            time.sleep(0.1)
            pi2go.setLED(i, 0, 0, 0)
        for i in range(4):
            pi2go.setLED(i, 0, 4095, 0) # set to Green
            time.sleep(0.1)
            pi2go.setLED(i, 0, 0, 0)
        for i in range(4):
            pi2go.setLED(i, 0, 0, 4095) # set to Blue
            time.sleep(0.1)
            pi2go.setLED(i, 0, 0, 0)
        for i in range(4):
            pi2go.setLED(i, 4095, 4095, 4095) # set to White
            time.sleep(0.1)
            pi2go.setLED(i, 0, 0, 0)

try:
    thread.start_new_thread(ufoLights)
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
                pi2go.setLED(0, LEDon, LEDoff, LEDoff)
                pi2go.spinRight(speed)
                time.sleep(2)
                pi2go.setAllLEDs(LEDoff, LEDoff, LEDoff)
            else:
                pi2go.setLED(3, LEDon, LEDon, LEDon)
                pi2go.forward(speed)
            pi2go.stop()
except:
    print "noooooo"

finally:
  pi2go.cleanup()
