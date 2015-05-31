import RPi.GPIO as GPIO, time 

# script gebruikt om het aantal cycles te bepalen en zo de LDR te kalibreren.
# setup function
def setup():
   global pinNr
   pinNr = 4
   GPIO.setmode(GPIO.BCM)


def RCtime():
   global pinNr
   global oldVal

   measurement = 0

   GPIO.setup(pinNr, GPIO.OUT)
   GPIO.output(pinNr, GPIO.LOW)
   time.sleep(0.1)

   GPIO.setup(pinNr, GPIO.IN)

   while(GPIO.input(pinNr)==GPIO.LOW):
      measurement += 1

   return measurement

#main function
setup()
while True:
   RCtime()
