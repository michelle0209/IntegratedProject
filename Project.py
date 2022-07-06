import pyfirmata
from time import sleep
port = 'COM6'
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

IRSensor=board.get_pin('d:13:i')
redLED=board.get_pin('d:12:o')
buzzer=board.get_pin('d:11:o')
firstServo=board.get_pin('p:10:s')
button=board.get_pin('d:9:i')

def setServoAngle(angle):
  firstServo.write(angle)
  sleep(0.01)

while True:
    sensorOuput=IRSensor.read()
    if not sensorOuput:
        print('Obstacle')
        sleep(1)
        redLED.write(1)
        buzzer.write(1)
        sleep(2)
        buzzer.write(0)
        for i in range(0, 91,1):
            setServoAngle(i)
        sleep(2)
        for i in range(90, 0,-1):
            setServoAngle(i)
        redLED.write(0)
    else:
        print('Clear')
        sleep(1)
