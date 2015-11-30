import pi2go, time, thread

pi2go.init()

speed = 40
LEDon = 4095
LEDoff = 0

def ufoLights():
    while True:
        for i in range(4):
            pi2go.setLED(i, 4095, 0, 0) # set to Red
            time.sleep(0.1)
            pi2go.setLED(i, 0, 0, 0)

def moveAround():
    while True:
        while not (pi2go.irLeft() or pi2go.irRight() or pi2go.irCentre()):
            if pi2go.getDistance() <= 2.0:
                pi2go.spinLeft(speed)
                time.sleep(1.5)
            else:
                pi2go.forward(speed)
        pi2go.stop()
        if pi2go.irLeft():
            while pi2go.irLeft():
                pi2go.spinRight(speed)
                time.sleep(0.5)
            pi2go.stop()
        if pi2go.irRight():
            while pi2go.irRight():
                pi2go.spinLeft(speed)
                time.sleep(0.5)
            pi2go.stop()
        if pi2go.irCentre():
            while pi2go.irCentre():
                pi2go.reverse(speed)
                time.sleep(2)
                pi2go.spinLeft(speed)
                time.sleep(1)
            pi2go.stop()

try:
    thread.start_new_thread(ufoLights, ())
    thread.start_new_thread(moveAround, ())
except KeyboardInterrupt:
    pass
except:
    print "Error: unable to start thread"
finally:
    pi2go.cleanup()
